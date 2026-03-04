"""
PleadingPaper — California-style legal pleading paper renderer.

Renders PDFs with 28 numbered lines, double vertical rules on the left,
a right-margin rule, headers, footers, and proper legal formatting.
Content-agnostic: all text is passed in via method calls.
"""

import io
import re

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import black
from reportlab.pdfgen import canvas


PAGE_W, PAGE_H = letter
MARGIN_LEFT = 1.0 * inch
MARGIN_RIGHT = 0.5 * inch

LINE_SPACING = 24
NUM_LINES = 28
FONT_SIZE = 12

TEXT_START_Y = PAGE_H - 1.05 * inch
TEXT_END_Y = TEXT_START_Y - (NUM_LINES - 1) * LINE_SPACING

VERT_LINE_LEFT = MARGIN_LEFT + 0.30 * inch
VERT_LINE_RIGHT = MARGIN_LEFT + 0.35 * inch
LINE_NUM_X = VERT_LINE_LEFT - 0.08 * inch

CONTENT_LEFT = VERT_LINE_RIGHT + 0.10 * inch
CONTENT_RIGHT = PAGE_W - MARGIN_RIGHT
CONTENT_WIDTH = CONTENT_RIGHT - CONTENT_LEFT

FOOTER_RULE_Y = TEXT_END_Y - 12
FOOTER_PAGE_Y = FOOTER_RULE_Y - 16
FOOTER_TITLE_Y = FOOTER_PAGE_Y - 18


class PleadingPaper:
    """Renders California-style pleading paper to a BytesIO buffer."""

    def __init__(self, buffer: io.BytesIO, doc_title: str = ""):
        self.buffer = buffer
        self.c = canvas.Canvas(buffer, pagesize=letter)
        self.page_num = 0
        self.current_line = 0
        self.doc_title = doc_title
        self._start_new_page()

    def _start_new_page(self):
        if self.page_num > 0:
            self.c.showPage()
        self.page_num += 1
        self.current_line = 0
        self._draw_page_frame()

    def _draw_page_frame(self):
        c = self.c
        c.setStrokeColor(black)
        c.setLineWidth(0.5)

        top_y = PAGE_H
        bot_y = 0

        # Double vertical rules on left
        c.line(VERT_LINE_LEFT, top_y, VERT_LINE_LEFT, bot_y)
        c.line(VERT_LINE_RIGHT, top_y, VERT_LINE_RIGHT, bot_y)
        # Right margin rule
        c.line(CONTENT_RIGHT, top_y, CONTENT_RIGHT, bot_y)

        # Line numbers
        c.setFont("Helvetica", 10)
        for i in range(NUM_LINES):
            y = TEXT_START_Y - i * LINE_SPACING
            c.drawRightString(LINE_NUM_X, y, str(i + 1))

        # Footer rule
        c.setLineWidth(0.5)
        c.line(VERT_LINE_RIGHT, FOOTER_RULE_Y, CONTENT_RIGHT, FOOTER_RULE_Y)

        # Page number
        center_x = (VERT_LINE_LEFT + CONTENT_RIGHT) / 2
        c.setFont("Helvetica", 10)
        c.drawCentredString(center_x, FOOTER_PAGE_Y, f"Page {self.page_num}")

        # Document title in footer
        if self.doc_title:
            c.setFont("Helvetica", 9)
            c.drawCentredString(center_x, FOOTER_TITLE_Y, self.doc_title)

    def _line_y(self, idx):
        return TEXT_START_Y - idx * LINE_SPACING

    def _ensure_line(self):
        if self.current_line >= NUM_LINES:
            self._start_new_page()

    def write_line(self, text, bold=False, font="Times-Roman", size=FONT_SIZE,
                   italic=False, center=False, right=False, indent=0,
                   underline=False):
        self._ensure_line()
        y = self._line_y(self.current_line)
        c = self.c

        if bold and italic:
            fn = "Times-BoldItalic"
        elif bold:
            fn = "Times-Bold"
        elif italic:
            fn = "Times-Italic"
        else:
            fn = font

        c.setFont(fn, size)
        x = CONTENT_LEFT + indent

        if center:
            cx = CONTENT_LEFT + CONTENT_WIDTH / 2
            c.drawCentredString(cx, y, text)
        elif right:
            c.drawRightString(CONTENT_RIGHT, y, text)
        else:
            c.drawString(x, y, text)

        if underline:
            tw = c.stringWidth(text, fn, size)
            if center:
                ux = cx - tw / 2
            elif right:
                ux = CONTENT_RIGHT - tw
            else:
                ux = x
            c.setLineWidth(0.5)
            c.line(ux, y - 1.5, ux + tw, y - 1.5)

        self.current_line += 1

    def blank_line(self):
        self._ensure_line()
        self.current_line += 1

    def write_wrapped(self, text, bold=False, font="Times-Roman", size=FONT_SIZE,
                      italic=False, indent=0, first_indent=36):
        avail = CONTENT_WIDTH - indent
        segs = self._parse_segments(text)
        lines = self._wrap_segments(segs, avail, first_indent, size)
        c = self.c

        for i, parts in enumerate(lines):
            self._ensure_line()
            y = self._line_y(self.current_line)
            x = CONTENT_LEFT + indent
            if i == 0:
                x += first_indent

            for pt, ps in parts:
                if ps == "bi":
                    pfn = "Times-BoldItalic"
                elif ps == "b":
                    pfn = "Times-Bold"
                elif ps == "i":
                    pfn = "Times-Italic"
                else:
                    pfn = "Times-Roman"
                c.setFont(pfn, size)
                c.drawString(x, y, pt)
                x += c.stringWidth(pt, pfn, size)

            self.current_line += 1

    def _parse_segments(self, text):
        segs = []
        pat = r"<<(b|i|bi):([^>]*)>>"
        last = 0
        for m in re.finditer(pat, text):
            if m.start() > last:
                segs.append((text[last:m.start()], "r"))
            segs.append((m.group(2), m.group(1)))
            last = m.end()
        if last < len(text):
            segs.append((text[last:], "r"))
        return segs

    def _wrap_segments(self, segs, avail, fi, size):
        c = self.c
        lines, cur = [], []
        cw = fi

        def _font_for_style(s):
            if s == "bi":
                return "Times-BoldItalic"
            elif s == "b":
                return "Times-Bold"
            elif s == "i":
                return "Times-Italic"
            return "Times-Roman"

        for st, ss in segs:
            fn = _font_for_style(ss)
            words = st.split(" ")
            for wi, w in enumerate(words):
                if wi > 0:
                    w = " " + w
                ww = c.stringWidth(w, fn, size)
                if cw + ww > avail and cur:
                    lines.append(cur)
                    cur = []
                    cw = 0
                    if w.startswith(" "):
                        w = w[1:]
                        ww = c.stringWidth(w, fn, size)
                cur.append((w, ss))
                cw += ww
        if cur:
            lines.append(cur)
        return lines

    def draw_horizontal_rule(self):
        self._ensure_line()
        y = self._line_y(self.current_line) + 6
        self.c.setLineWidth(0.5)
        self.c.line(CONTENT_LEFT, y, CONTENT_RIGHT, y)
        self.current_line += 1

    def _truncate_to_width(self, text, font, size, max_width):
        """Truncate text to fit within max_width, adding ellipsis if needed."""
        c = self.c
        if c.stringWidth(text, font, size) <= max_width:
            return text
        while text and c.stringWidth(text + "...", font, size) > max_width:
            text = text[:-1]
        return text + "..."

    def draw_caption_block(self, left, right):
        """Draw a case caption with left/right columns.

        Each side is a list of tuples: (text, bold, italic).
        A vertical bracket ")" is drawn between the columns.
        """
        c = self.c
        mid = CONTENT_LEFT + CONTENT_WIDTH * 0.45
        bx = mid - 10
        rx = mid + 5
        left_max_width = bx - CONTENT_LEFT - 5
        right_max_width = CONTENT_RIGHT - rx - 5
        tot = max(len(left), len(right))

        for i in range(tot):
            self._ensure_line()
            y = self._line_y(self.current_line)

            if i < len(left):
                lt, lb, li = left[i]
                if lb and li:
                    fn = "Times-BoldItalic"
                elif lb:
                    fn = "Times-Bold"
                elif li:
                    fn = "Times-Italic"
                else:
                    fn = "Times-Roman"
                c.setFont(fn, FONT_SIZE)
                lt = self._truncate_to_width(lt, fn, FONT_SIZE, left_max_width)
                c.drawString(CONTENT_LEFT, y, lt)

            # Bracket
            c.setFont("Times-Roman", FONT_SIZE)
            c.drawString(bx, y, ")")

            if i < len(right):
                rt, rb, ri = right[i]
                if rb and ri:
                    fn = "Times-BoldItalic"
                elif rb:
                    fn = "Times-Bold"
                elif ri:
                    fn = "Times-Italic"
                else:
                    fn = "Times-Roman"
                c.setFont(fn, FONT_SIZE)
                rt = self._truncate_to_width(rt, fn, FONT_SIZE, right_max_width)
                c.drawString(rx, y, rt)

            self.current_line += 1

    def save(self):
        self.c.save()

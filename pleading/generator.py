"""
Random lawsuit generator.

Picks random components from data pools and assembles a complete
California-style legal pleading PDF using PleadingPaper.
"""

import io
import random
from datetime import datetime, timedelta

from pleading.paper import PleadingPaper
from pleading import data


def _random_plaintiff_name():
    first = random.choice(data.PLAINTIFF_FIRST_NAMES)
    middle = random.choice(data.PLAINTIFF_MIDDLE_INITIALS)
    last = random.choice(data.PLAINTIFF_LAST_NAMES)
    return f"{first} {middle} {last}"


def _random_date():
    days_ago = random.randint(30, 365 * 2)
    d = datetime.now() - timedelta(days=days_ago)
    return d.strftime("%B %d, %Y")


def _random_case_number():
    year = datetime.now().year
    seq = random.randint(10000, 99999)
    prefix = random.choice(["BC", "CV", "CIV", "SC"])
    return f"{prefix}{year}{seq}"


def _ordinal(n):
    """Return ordinal word for cause of action numbering."""
    words = {1: "FIRST", 2: "SECOND", 3: "THIRD", 4: "FOURTH", 5: "FIFTH"}
    return words.get(n, f"{n}TH")


def _wrap_caption_text(text, max_chars=30):
    """Word-wrap text for caption columns, returning list of lines."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        if current and len(current) + 1 + len(word) > max_chars:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}" if current else word
    if current:
        lines.append(current)
    return lines


def generate_lawsuit_pdf():
    """Generate a complete random lawsuit PDF. Returns a BytesIO buffer."""
    buf = io.BytesIO()

    # Pick random components
    plaintiff = _random_plaintiff_name()
    plaintiff_upper = plaintiff.upper()
    defendant = random.choice(data.DEFENDANT_NAMES)
    court = random.choice(data.COURTS)
    case_type = random.choice(data.CASE_TYPES)
    judge = random.choice(data.JUDGE_NAMES)
    attorney = random.choice(data.ATTORNEY_FIRMS)
    case_number = _random_case_number()
    amount = random.choice(data.DAMAGE_AMOUNTS)
    location = random.choice(data.LOCATIONS)
    incident_date = _random_date()

    doc = PleadingPaper(buf, doc_title=case_type["title"])

    # ── Attorney Header ──
    doc.write_line(attorney["name"])
    doc.write_line(f"State Bar No. {attorney['bar']}")
    doc.write_line(attorney["address"])
    doc.write_line(attorney["city"])
    doc.write_line(f"Telephone: {attorney['phone']}")
    doc.blank_line()
    doc.write_line(f"Attorney for Plaintiff {plaintiff_upper}")
    doc.blank_line()

    # ── Court ──
    doc.write_line(court["line1"], bold=True, center=True)
    doc.write_line(court["line2"], bold=True, center=True)
    doc.blank_line()

    # ── Caption Block ──
    # Wrap long defendant names across multiple lines
    def_lines = _wrap_caption_text(f"{defendant},", max_chars=35)

    left_caption = [
        (f"{plaintiff_upper},", False, False),
        ("", False, False),
        ("     Plaintiff,", False, False),
        ("", False, False),
        ("  v.", False, False),
        ("", False, False),
    ]
    for dl in def_lines:
        left_caption.append((dl, False, False))
    left_caption.append(("", False, False))
    left_caption.append(("     Defendant.", False, False))

    # Wrap long case titles across multiple lines
    title_lines = _wrap_caption_text(case_type["title"], max_chars=30)

    right_caption = [
        (f"Case No. {case_number}", False, False),
        ("", False, False),
    ]
    for tl in title_lines:
        right_caption.append((tl, True, False))
    # Pad to align with left side
    while len(right_caption) < len(left_caption) - 2:
        right_caption.append(("", False, False))
    right_caption.append((f"Judge: {judge}", False, False))
    doc.draw_caption_block(left_caption, right_caption)
    doc.draw_horizontal_rule()

    # ── General Allegations ──
    doc.blank_line()
    doc.write_line("GENERAL ALLEGATIONS", bold=True, center=True)
    doc.blank_line()

    # Fill and write fact paragraphs
    para_num = 1
    for fact_template in case_type["facts"]:
        text = fact_template.format(
            plaintiff=plaintiff_upper,
            defendant=defendant,
            date=incident_date,
            amount=amount,
            location=location,
        )
        doc.write_wrapped(
            f"{para_num}. {text}",
            first_indent=36,
        )
        doc.blank_line()
        para_num += 1

    # ── Causes of Action ──
    for i, cause in enumerate(case_type["causes"], 1):
        doc.write_line(
            f"{_ordinal(i)} CAUSE OF ACTION",
            bold=True,
            center=True,
        )
        # Extract the parenthetical from the heading if present
        heading = cause["heading"]
        paren_start = heading.find("(")
        if paren_start != -1:
            doc.write_line(heading[paren_start:], center=True, italic=True)
        doc.blank_line()

        # Re-allege paragraph
        doc.write_wrapped(
            f"{para_num}. {plaintiff_upper} re-alleges and incorporates by "
            f"reference each and every allegation set forth in Paragraphs 1 "
            f"through {para_num - 1} above, as though fully set forth herein.",
            first_indent=36,
        )
        doc.blank_line()
        para_num += 1

        # Cause body
        body = cause["body"].format(
            plaintiff=plaintiff_upper,
            defendant=defendant,
            date=incident_date,
            amount=amount,
            location=location,
        )
        doc.write_wrapped(f"{para_num}. {body}", first_indent=36)
        doc.blank_line()
        para_num += 1

    # ── Prayer for Relief ──
    doc.write_line("PRAYER FOR RELIEF", bold=True, center=True)
    doc.blank_line()
    doc.write_wrapped(
        f"WHEREFORE, Plaintiff {plaintiff_upper} prays for judgment against "
        f"Defendant {defendant} as follows:",
        first_indent=36,
    )
    doc.blank_line()

    for j, prayer_item in enumerate(case_type["prayer"], 1):
        text = prayer_item.format(
            plaintiff=plaintiff_upper,
            defendant=defendant,
            amount=amount,
        )
        doc.write_wrapped(f"{j}. {text}", first_indent=36)

    # ── Signature Block ──
    doc.blank_line()
    doc.blank_line()
    doc.write_line(f"DATED: {datetime.now().strftime('%B %d, %Y')}")
    doc.write_line("Respectfully submitted,")
    doc.blank_line()
    doc.blank_line()
    doc.write_line("_____________________________________")
    doc.write_line(attorney["name"])
    doc.write_line(f"Attorney for Plaintiff {plaintiff_upper}")

    doc.save()
    buf.seek(0)
    return buf

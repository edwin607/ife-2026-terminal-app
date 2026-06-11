#!/usr/bin/env python3
"""Generate The Hallucination Trap activity PDF for IFE 2026 curriculum."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus.flowables import Flowable
import os

OUTPUT_DIR = "/Users/eolivera/Documents/Clients/Cambio Labs/IFE"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "hallucination_trap_activity.pdf")

BG_DARK = HexColor("#0f172a")
BG_CARD = HexColor("#1e293b")
ACCENT_BLUE = HexColor("#3b82f6")
ACCENT_PURPLE = HexColor("#8b5cf6")
ACCENT_PINK = HexColor("#ec4899")
ACCENT_GREEN = HexColor("#22c55e")
ACCENT_RED = HexColor("#ef4444")
ACCENT_YELLOW = HexColor("#eab308")
TEXT_WHITE = HexColor("#f8fafc")
TEXT_SLATE = HexColor("#94a3b8")
TEXT_DIM = HexColor("#64748b")
BORDER = HexColor("#334155")


def build_styles():
    base = getSampleStyleSheet()

    def add(name, **kw):
        base.add(ParagraphStyle(name, **kw))

    add("IFE_Title", fontName="Helvetica-Bold", fontSize=28, textColor=TEXT_WHITE, spaceAfter=4, alignment=TA_LEFT)
    add("IFE_Subtitle", fontName="Helvetica", fontSize=13, textColor=ACCENT_BLUE, spaceAfter=16, alignment=TA_LEFT)
    add("IFE_SectionHeader", fontName="Helvetica-Bold", fontSize=14, textColor=ACCENT_PURPLE, spaceBefore=14, spaceAfter=6)
    add("IFE_BodyText", fontName="Helvetica", fontSize=11, textColor=TEXT_SLATE, spaceAfter=6, alignment=TA_JUSTIFY, leading=16)
    add("IFE_BulletItem", fontName="Helvetica", fontSize=11, textColor=TEXT_SLATE, leftIndent=20, spaceAfter=4, leading=15, bulletIndent=8)
    add("IFE_MonoText", fontName="Courier", fontSize=9, textColor=ACCENT_GREEN, spaceAfter=4, leading=13)
    add("IFE_QuoteText", fontName="Helvetica-Oblique", fontSize=12, textColor=ACCENT_YELLOW, leftIndent=24, rightIndent=24, spaceBefore=10, spaceAfter=10, leading=17)
    add("IFE_CaptionSmall", fontName="Helvetica", fontSize=9, textColor=TEXT_DIM, spaceAfter=4)
    add("IFE_TableCell", fontName="Helvetica", fontSize=10, textColor=TEXT_SLATE, leading=14)
    add("IFE_TableCellBold", fontName="Helvetica-Bold", fontSize=10, textColor=TEXT_WHITE, leading=14)
    add("IFE_TagLabel", fontName="Helvetica-Bold", fontSize=8, textColor=white, alignment=TA_CENTER)

    return base


def make_header_table():
    """Top banner with capsule tag and title."""
    tag = Paragraph("CAPSULE 08: AI RELIABILITY", styles["IFE_TagLabel"])
    tag_table = Table([[tag]], colWidths=[6.5 * inch])
    tag_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ACCENT_BLUE),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("ROUNDEDCORNERS", [4]),
    ]))

    title = Paragraph("The Hallucination Trap", styles["IFE_Title"])
    subtitle = Paragraph("Teaching founders to spot and verify AI fabrications", styles["IFE_Subtitle"])

    return [tag_table, Spacer(0, 12), title, subtitle]


def make_quote_block(text):
    line = HRFlowable(width="100%", thickness=1, color=ACCENT_YELLOW, spaceBefore=6, spaceAfter=6)
    quote = Paragraph(text, styles["IFE_QuoteText"])
    return [line, quote, line]


def make_section(header, body_items):
    items = [Paragraph(header, styles["IFE_SectionHeader"])]
    for item in body_items:
        if item.startswith("•"):
            items.append(Paragraph(item, styles["IFE_BulletItem"]))
        elif item.startswith("```"):
            continue
        elif item.strip() == "":
            items.append(Spacer(0, 4))
        else:
            items.append(Paragraph(item, styles["IFE_BodyText"]))
    return items


def make_prompt_table(prompts):
    """Two-column table for prompt comparison."""
    header_left = Paragraph("PROMPT 1: The Claim", styles["IFE_TableCellBold"])
    header_right = Paragraph("PROMPT 2: The Verifier", styles["IFE_TableCellBold"])

    body_left = Paragraph(prompts[0], styles["IFE_TableCell"])
    body_right = Paragraph(prompts[1], styles["IFE_TableCell"])

    data = [
        [header_left, header_right],
        [body_left, body_right],
    ]

    t = Table(data, colWidths=[3.2 * inch, 3.2 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (1, 0), BG_CARD),
        ("TEXTCOLOR", (0, 0), (1, 0), TEXT_WHITE),
        ("BACKGROUND", (0, 1), (0, 1), HexColor("#1a1a2e")),
        ("BACKGROUND", (1, 1), (1, 1), HexColor("#1a2e1a")),
        ("TEXTCOLOR", (0, 1), (-1, -1), TEXT_SLATE),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    return t


def make_cli_block(commands):
    """Code-style block for CLI commands."""
    lines = []
    for cmd in commands:
        lines.append(Paragraph(cmd, styles["IFE_MonoText"]))
    return lines


def make_footer():
    line = HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=12, spaceAfter=6)
    footer = Paragraph("IFE 2026 — AI Tools Curriculum  |  Free / API-Only  |  llm CLI + Groq", styles["IFE_CaptionSmall"])
    return [line, footer]


def build():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
    )

    global styles
    styles = build_styles()

    story = []

    # Background color trick: reportlab doesn't support full-page bg easily,
    # so we use a table as background frame.
    # Instead, keep it clean white-bg with dark-themed elements.

    story.extend(make_header_table())
    story.append(Spacer(0, 8))

    # Hook
    story.extend(make_quote_block(
        '"Your pitch deck has numbers in it. If your AI made them up, investors will destroy you. '
        "Let's build a BS detector.\""
    ))

    story.append(Spacer(0, 10))

    # Overview
    story.extend(make_section("Overview", [
        "Students learn that AI models confidently generate false information — and how to build a verification "
        "layer into their everyday business workflows using free tools they already have.",
        "",
        "• Duration: 25 minutes",
        "• Tools: llm CLI (Groq free tier — no credit card)",
        "• Setup: 5 minutes (already installed from Week 1)",
        "• Format: Pairs, hands-on with terminals",
        "• Fits: Week 2 or 3, alongside The Translator or Spy Agency",
    ]))

    # Learning Objectives
    story.extend(make_section("Learning Objectives", [
        "• Understand what AI hallucination is and why it happens",
        "• Experience firsthand how confidently wrong an AI can be",
        "• Build a two-prompt verification workflow",
        "• Apply skepticism to AI outputs in business contexts",
        "• Connect AI literacy to real founder risk (pitch decks, research, customer claims)",
    ]))

    # Activity Flow
    story.extend(make_section("Activity Flow (25 min)", [
        "Step 1 — The Trap (5 min)",
        "Each pair picks a business claim (provided or their own). Examples:",
        "• \"70% of startups fail in year one\"",
        "• \"The average small business spends $5,000/month on marketing\"",
        "• \"90% of consumers trust online reviews as much as personal recommendations\"",
        "",
        "Step 2 — First Prompt (5 min)",
        "Students send the claim to the AI asking: \"Is this true? Cite your sources.\"",
        "The AI responds with a confident, plausible-sounding answer — often with fabricated citations.",
        "",
        "Step 3 — The Reveal (5 min)",
        "Pairs compare answers. The facilitator reveals: the AI just made it up. No sources exist.",
        "Discussion: Why does the AI sound so sure when it's wrong?",
        "",
        "Step 4 — The Verifier (5 min)",
        "Students run a second prompt that cross-checks the first answer. They compare side by side.",
        "",
        "Step 5 — Debrief (5 min)",
        "What did this teach you about using AI for business research? How would you protect your pitch deck?",
    ]))

    # Prompts
    story.append(Paragraph("The Two Prompts", styles["IFE_SectionHeader"]))
    story.append(Spacer(0, 6))
    story.append(make_prompt_table([
        "You are a business research assistant. I need to verify this claim for a pitch deck: \"70% of startups fail in their first year.\" Is this accurate? Please cite specific sources and studies.",
        "You are a fact-checker. Someone claims that 70% of startups fail in their first year. What does actual data from reliable sources (SBA, CB Insights, Bureau of Labor Statistics) say? Flag any common misconceptions.",
    ]))
    story.append(Spacer(0, 6))
    story.append(Paragraph("Run them back-to-back and compare the answers.", styles["IFE_CaptionSmall"]))

    story.append(Spacer(0, 14))

    # CLI Commands
    story.extend(make_section("CLI Commands", [
        "# Set your key once:",
    ]))
    story.extend(make_cli_block([
        "$ llm keys set groq",
        "$ llm -m groq \"You are a business researcher. Is it true that 70% of startups fail in year one? Cite sources.\"",
        "",
        "# Then the verifier:",
        "$ llm -m groq \"You are a fact-checker. What does actual data from SBA and BLS say about startup failure rates?\"",
    ]))

    # Why This Works
    story.extend(make_section("Why This Works", [
        "• Entrepreneurship-first: Opens with a real founder problem (pitch deck credibility)",
        "• Zero new setup: Uses llm CLI from Week 1, Groq free tier",
        "• Visceral: Students see the hallucination with their own eyes",
        "• Transferable: The two-prompt pattern applies to any research task",
        "• Complements existing capsules: Pairs with Bias Detective (ethics) and Neural Sandbox (context limits)",
    ]))

    # Fallbacks
    story.extend(make_section("Offline / No-Internet Fallback", [
        "• Print pre-generated AI responses (one hallucinated, one verified) on cards",
        "• Students play detective: which answer is fabricated?",
        "• Use sticky notes to map out what a \"verification layer\" looks like on paper",
        "• Role-play: one student is the AI, another is the verifier, third is the founder",
    ]))

    story.append(Spacer(0, 16))
    story.extend(make_footer())

    doc.build(story)
    print(f"PDF generated: {OUTPUT_PATH}")


if __name__ == "__main__":
    build()

"""Regenerate the investigation graphics and assessments from editable sources.

Optional switches allow graphics and PDFs to be built in separate environments.
"""
from pathlib import Path
from html import escape
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
GRAPHICS = [
    'mapmyrun-quality-investigation-project-card',
    'Michael_Jensen_MapMyRun_Balanced_Quality_Assessment',
    'Michael_Jensen_MapMyRun_Apple_Health_User_Trust',
]


def render_graphics():
    import cairosvg
    for name in GRAPHICS:
        cairosvg.svg2png(url=str(ROOT / f'{name}.svg'), write_to=str(ROOT / f'{name}.png'))


def render_reports():
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image

    navy = colors.HexColor('#102338')
    teal = colors.HexColor('#147e74')
    slate = colors.HexColor('#405468')
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='MainTitle', fontName='Helvetica-Bold', fontSize=25, leading=29, textColor=navy, spaceAfter=12))
    styles.add(ParagraphStyle(name='Section', fontName='Helvetica-Bold', fontSize=17, leading=21, textColor=navy, spaceBefore=6, spaceAfter=12))
    styles.add(ParagraphStyle(name='Subsection', fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=teal, spaceBefore=13, spaceAfter=6))
    styles.add(ParagraphStyle(name='Copy', fontName='Helvetica', fontSize=9.2, leading=12.3, textColor=slate, spaceAfter=8))
    styles.add(ParagraphStyle(name='CellCopy', fontName='Helvetica', fontSize=8.7, leading=11.5, textColor=navy))
    styles.add(ParagraphStyle(name='CellHead', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=colors.white))
    styles.add(ParagraphStyle(name='BulletCopy', parent=styles['Copy'], leftIndent=10, firstLineIndent=-8, spaceAfter=5))

    def inline(text):
        return escape(text)

    def footer(canvas, doc):
        w, h = doc.pagesize
        canvas.saveState()
        for x, width, color in [(0, w*.35, '#34c6b3'),(w*.35,w*.35,'#398eff'),(w*.7,w*.3,'#eab45b')]:
            canvas.setFillColor(colors.HexColor(color)); canvas.rect(x,h-5,width,5,fill=1,stroke=0)
        canvas.setStrokeColor(colors.HexColor('#d4dfe7')); canvas.line(46,38,w-46,38)
        canvas.setFont('Helvetica',7.5); canvas.setFillColor(slate)
        canvas.drawString(46,25,'Michael D. Jensen | Independent MapMyRun investigation | Revised October 15, 2026')
        canvas.drawRightString(w-46,25,str(doc.page))
        canvas.restoreState()

    for source, target in [('brief.md','Michael_Jensen_MapMyRun_Weekend_Quality_Assessment.pdf'),('assessment.md','Michael_Jensen_MapMyRun_Senior_QE_Assessment.pdf')]:
        doc = SimpleDocTemplate(str(ROOT/target), pagesize=(612,792), rightMargin=46,leftMargin=46,topMargin=40,bottomMargin=51,
            title='MapMyRun Quality Investigation - '+('Assessment brief' if source=='brief.md' else 'Methods, evidence, and quality assessment'),
            author='Michael D. Jensen',subject='Independent, evidence-bounded field investigation',invariant=1)
        story=[]
        lines=(ROOT/'docs'/source).read_text(encoding='utf-8').splitlines()
        i=0
        while i<len(lines):
            line=lines[i].strip()
            if not line:
                i+=1;continue
            if line=='<!-- pagebreak -->':
                story.append(PageBreak());i+=1;continue
            if line.startswith('|'):
                rows=[]
                while i<len(lines) and lines[i].strip().startswith('|'):
                    row=[c.strip() for c in lines[i].strip().strip('|').split('|')]
                    if not all(re.fullmatch(r':?-+:?',c) for c in row):rows.append(row)
                    i+=1
                n=len(rows[0]); widths=([122,199,199] if n==3 else [150,370] if n==2 else [169]+[117]*3)
                table=Table([[Paragraph(inline(c),styles['CellHead' if r==0 else 'CellCopy']) for c in row] for r,row in enumerate(rows)],colWidths=widths,repeatRows=1,hAlign='LEFT')
                table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),navy),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#f0f5f7'),colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,-1),(-1,-1),.5,colors.HexColor('#cad8e2'))]))
                story.extend([table,Spacer(1,11)]);continue
            if line.startswith('!['):
                target_image=re.search(r'\]\(([^)]+)\)',line).group(1)
                im=Image(str((ROOT/'docs'/target_image).resolve()),width=520,height=292.5)
                im.hAlign='CENTER';story.extend([im,Spacer(1,10)]);i+=1;continue
            if line.startswith('# '):style='MainTitle';line=line[2:]
            elif line.startswith('## '):style='Section';line=line[3:]
            elif line.startswith('### '):style='Subsection';line=line[4:]
            elif line.startswith('- '):style='BulletCopy';line='- '+line[2:]
            else:
                style='Copy'
                while i+1<len(lines) and lines[i+1].strip() and not lines[i+1].startswith(('#','|','- ','![','<!--')):
                    i+=1;line+=' '+lines[i].strip()
            story.append(Paragraph(inline(line),styles[style]));i+=1
        doc.build(story,onFirstPage=footer,onLaterPages=footer)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--graphics-only',action='store_true')
    group.add_argument('--reports-only',action='store_true')
    args=parser.parse_args()
    if not args.reports_only:render_graphics()
    if not args.graphics_only:render_reports()

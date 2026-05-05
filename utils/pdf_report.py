import io
import datetime
from fpdf import FPDF


class SIBOReport(FPDF):
    """Custom PDF class for the SIBO/IMO diagnostic report."""

    def header(self):
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, 'SIBO & IMO Clinical AI System  |  Diagnostic Report', align='C')
        self.ln(4)
        self.set_draw_color(56, 189, 248)
        self.set_line_width(0.4)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(6)

    def footer(self):
        self.set_y(-25)
        self.set_font('Helvetica', 'I', 7)
        self.set_text_color(180, 180, 180)
        self.multi_cell(0, 3.5,
                        'DISCLAIMER: This report is for educational purposes only and should not '
                        'be used as a substitute for professional medical advice, diagnosis, or treatment.',
                        align='C')
        self.set_font('Helvetica', '', 7)
        self.cell(0, 5, f'Page {self.page_no()}', align='C')


def generate_pdf_report(patient_data):
    """
    Generate a PDF report from patient data dict.

    patient_data = {
        'name': str,
        'gender': str,
        'inputs': dict of feature->value,
        'diagnosis': str,
        'probabilities': dict of class->percentage,
    }

    Returns bytes of the PDF.
    """
    pdf = SIBOReport()
    pdf.set_auto_page_break(auto=True, margin=30)
    pdf.add_page()

    # ===== Title =====
    pdf.set_font('Helvetica', 'B', 22)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 14, 'Breath Test Analysis Report', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    # Date
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(100, 100, 100)
    now = datetime.datetime.now().strftime('%B %d, %Y at %H:%M')
    pdf.cell(0, 6, f'Generated: {now}', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)

    # ===== Patient Info =====
    pdf.set_fill_color(240, 245, 255)
    pdf.set_font('Helvetica', 'B', 13)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 10, '   Patient Information', fill=True, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(50, 50, 50)
    gender = patient_data.get('gender', 'N/A')
    age = patient_data.get('inputs', {}).get('Age', 'N/A')

    pdf.cell(60, 8, f'Gender: {gender}')
    pdf.cell(60, 8, f'Age: {age}', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)

    # ===== Test Values =====
    pdf.set_fill_color(240, 245, 255)
    pdf.set_font('Helvetica', 'B', 13)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 10, '   Breath Test Values', fill=True, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(50, 50, 50)

    inputs = patient_data.get('inputs', {})

    # Table header
    pdf.set_fill_color(56, 189, 248)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(110, 8, '  Parameter', border=1, fill=True)
    pdf.cell(70, 8, '  Value', border=1, fill=True, new_x="LMARGIN", new_y="NEXT")

    pdf.set_text_color(50, 50, 50)
    pdf.set_font('Helvetica', '', 10)
    fill = False
    for key, val in inputs.items():
        if fill:
            pdf.set_fill_color(248, 250, 252)
        else:
            pdf.set_fill_color(255, 255, 255)
        # Replace unicode subscripts for PDF compatibility
        display_key = key.replace('\u2082', '2').replace('\u2084', '4')
        pdf.cell(110, 7, f'  {display_key}', border=1, fill=True)
        pdf.cell(70, 7, f'  {val}', border=1, fill=True, new_x="LMARGIN", new_y="NEXT")
        fill = not fill

    pdf.ln(8)

    # ===== Diagnosis Result =====
    pdf.set_fill_color(240, 245, 255)
    pdf.set_font('Helvetica', 'B', 13)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 10, '   Prediction Result', fill=True, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)

    diagnosis = patient_data.get('diagnosis', 'N/A')
    pdf.set_font('Helvetica', 'B', 16)

    # Colour-code the diagnosis
    color_map = {
        'SIBO': (56, 189, 248),
        'IMO': (245, 158, 11),
        'SIBO & IMO': (239, 68, 68),
        'No Diagnosis': (34, 197, 94),
    }
    r, g, b = color_map.get(diagnosis, (100, 100, 100))
    pdf.set_text_color(r, g, b)
    pdf.cell(0, 10, f'Predicted Diagnosis: {diagnosis}', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    # Confidence scores
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 8, 'Confidence Scores:', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    probabilities = patient_data.get('probabilities', {})
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(50, 50, 50)
    for cls, pct in sorted(probabilities.items(), key=lambda x: -x[1]):
        bar_width = pct * 1.2  # scale to fit
        pdf.cell(50, 7, f'  {cls}:')
        # Draw bar background
        x, y = pdf.get_x(), pdf.get_y()
        pdf.set_fill_color(230, 230, 230)
        pdf.rect(x, y + 1, 120, 5, style='F')
        # Draw bar fill
        cr, cg, cb = color_map.get(cls, (100, 100, 100))
        pdf.set_fill_color(cr, cg, cb)
        pdf.rect(x, y + 1, max(bar_width, 0.5), 5, style='F')
        pdf.set_x(x + 125)
        pdf.cell(0, 7, f'{pct:.1f}%', new_x="LMARGIN", new_y="NEXT")

    pdf.ln(10)

    # ===== Disclaimer Box =====
    pdf.set_fill_color(255, 250, 230)
    pdf.set_draw_color(245, 158, 11)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_text_color(180, 120, 0)
    y_start = pdf.get_y()
    pdf.rect(10, y_start, 190, 18, style='D')
    pdf.set_xy(12, y_start + 2)
    pdf.multi_cell(186, 4.5,
                   'WARNING: This report is generated by an educational AI tool. '
                   'It is NOT a clinical diagnosis. Always consult a qualified '
                   'healthcare professional for medical decisions.',
                   align='C')

    # Return PDF bytes
    return pdf.output()

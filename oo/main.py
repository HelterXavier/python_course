from decimal import Decimal
from fpdf import FPDF


class Student:

    def __init__(self, inscription, name, course, subject, grade1, grade2, assignment_grade):
        self.__inscription = inscription
        self.__name = name
        self.__course = course
        self.__subject = subject
        self.__grade1 = Decimal(str(grade1))
        self.__grade2 = Decimal(str(grade2))
        self.__assignment_grade = Decimal(str(assignment_grade))

    def _calc_grade(self):
        media_final = (self.__grade1 + self.__grade2 +
                       self.__assignment_grade) / 3
        return round(media_final, 2)

    def _aprovado_reprovado(self):
        media_final = self._calc_grade()

        if media_final < 7:
            return 'Você foi reprovado!  ❌'
        elif media_final >= 7:
            return 'Você foi aprovado!  ✅'

    @property
    def show_infos(self):
        return {
            "inscription": self.__inscription,
            "name": self.__name,
            "course": self.__course,
            "subject": self.__subject,
            "grade1": self.__grade1,
            "grade2": self.__grade2,
            "assigment": self.__assignment_grade,
            "media_final": self._calc_grade()
        }


    @property
    def show_final_grade(self):
        return f'Sua média final é: {self._calc_grade()} \n {self._aprovado_reprovado()}'


def add_info_student(student, pdf):
    pdf.set_font("Helvetica", size=14)

    pdf.cell(200, 10, text=f'Matrícula: {student.show_infos["inscription"]}')
    pdf.ln(10)
    pdf.cell(200, 10, text=f'Nome: {student.show_infos["name"]}')
    pdf.ln(10)
    pdf.cell(200, 10, text=f'Curso: {student.show_infos["course"]}')
    pdf.ln(10)
    pdf.cell(200, 10, text=f'Matéria: {student.show_infos["subject"]}')
    pdf.ln(10)
    pdf.cell(200, 10, text=f'Nota 1: {student.show_infos["grade1"]}')
    pdf.ln(10)
    pdf.cell(200, 10, text=f'Nota 2: {student.show_infos["grade2"]}')
    pdf.ln(10)
    pdf.cell(200, 10, text=f'Nota do Trabalho: {student.show_infos["assigment"]}')
    pdf.ln(10)
    pdf.cell(200, 10, text=f'Média Final: {student.show_infos["media_final"]}')
    pdf.ln(10)


def save_to_dict(student, file='oo/student_report.pdf'):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()


    add_info_student(student, pdf)

    # Salva o PDF final
    pdf.output(file)
    print(f"Relatório completo gerado: {file}")


def start_execution():
    try:
        inscription = input('Matrícula: ')
        name = input('Nome (Aluno): ')
        course = input('Curso: ')
        subject = input('Matéria: ')
        grade_1 = input('Digite a nota da primeira prova: ')
        grade_2 = input('Digite a nota da segunda prova: ')
        assignment = input('Digite a nota do trabalho: ')
        student = Student(inscription, name, course, subject,
                          grade_1, grade_2, assignment)

        save_to_dict(student)

        print(student.show_final_grade)

    except Exception as err:
        print(f'Erro ao registrar Média do aluno. {err}')


start_execution()

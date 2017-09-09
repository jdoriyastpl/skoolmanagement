from rolepermissions.roles import AbstractUserRole


class Principal(AbstractUserRole):
    available_permissions = {
        'create_teacher_record': True,
        'edit_teacher_record':True,
        'create_student_record': True,
        'edit_student_record':True,
        'create_staff_record': True,
        'edit_staff_record':True,
    }


class Teacher(AbstractUserRole):
    available_permissions = {
        'create_teacher_record': False,
        'create_student_record': False,
        'create_staff_record': False,
    }

class Staff(AbstractUserRole):
    available_permissions = {
        'create_teacher_record': False,
        'create_student_record': False,
        'create_staff_record': False,
    }

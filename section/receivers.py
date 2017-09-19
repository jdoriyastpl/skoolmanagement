# In receivers.py
from django.dispatch import receiver
from section.signals import update_count
from student.models import Student
from section.models import Section

@receiver(update_count)
def update_student_count(sender, **kwargs):
    student_name = kwargs['name']
    standard= kwargs["standard"]
    section = kwargs["section"]
    print("inside reciver")

    if Section.objects.filter(standard=standard).filter(name=section).values_list("no_students", flat=True)==0:
        print("line 13")
        update_count = Section.objects.filter(standard=standard).filter(name=section)\
                                        .update(no_students = 1)
    else:
        print("line 17")
        section_count = Section.objects.filter(standard= standard).filter(name=section).values_list("no_students", flat=True).all()
        print(section_count[0])

        print(section_count[0])
        update_count = Section.objects.filter(standard=standard).filter(name=section)\
                                        .update(no_students=section_count[0]+1)

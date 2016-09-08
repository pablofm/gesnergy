import django_tables2 as tables
from lectures.models import Lecture


class LectureTable(tables.Table):
    actions = tables.TemplateColumn(
        '<span class="actions">'+
        '<a href="{% url "lecture_detail" lecture_id=record.id %}"><i class="fa fa-2x fa-eye action"></i></a>'+
        '<a href="{% url "lecture_update" lecture_id=record.id %}"><i class="fa fa-2x fa-pencil action"></i></a>'+
        '<a href="{% url "lecture_delete" lecture_id=record.id %}" ><i class="fa fa-2x fa-trash-o action"></i></a>'+
        '</span>'
    )

    class Meta:
        model = Lecture
        fields = ('day', 'lecture')

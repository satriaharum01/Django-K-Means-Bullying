from django.db import models
from django.conf import settings

# Create your models here.

class m_data(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    s_fisik = models.IntegerField(max_length=2, blank=True, null=True)
    s_verbal = models.IntegerField(max_length=2, blank=True, null=True)
    s_psikologis = models.IntegerField(max_length=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'data_history'
        
    
class m_kuesioner(models.Model):
    
    QUESTION_TYPES = [
        ('fisik', 'Fisik'),
        ('psikologis', 'Psikologis'),
        ('verbal', 'Verbal'),
    ]
    
    question_text = models.CharField(max_length=100)  # Teks pertanyaan
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default='fisik')  # Jenis bullying

    def __str__(self):
        return f"{self.question_text} ({self.get_question_type_display()})"
    
    class Meta:
        db_table = 'kuesioner'

class m_response(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Menghubungkan ke CustomUser
    kuesioner = models.ForeignKey(m_kuesioner, on_delete=models.CASCADE)  # Menghubungkan ke pertanyaan kuesioner
    answer = models.IntegerField()  # Jawaban (misalnya, skala 1-5)
    submission_date = models.DateTimeField(auto_now_add=True)  # Waktu pengisian

    def __str__(self):
        return f"Response by {self.user.email} for question {self.kuesioner.id}"
    
    class Meta:
        db_table = 'responses'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    article_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    consumer = models.ForeignKey('Consumer', models.DO_NOTHING, blank=True, null=True)
    apply_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class Choice(models.Model):
    question = models.ForeignKey('Question', models.DO_NOTHING, blank=True, null=True)
    choice1 = models.CharField(max_length=80, blank=True, null=True)
    choice2 = models.CharField(max_length=80, blank=True, null=True)
    choice3 = models.CharField(max_length=80, blank=True, null=True)
    choice4 = models.CharField(max_length=80, blank=True, null=True)
    standard_answer = models.CharField(max_length=255, blank=True, null=True)
    hard = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'choice'


class Consumer(models.Model):
    consumer_id = models.BigAutoField(primary_key=True)
    consumer_account = models.CharField(max_length=40, blank=True, null=True)
    consumer_name = models.CharField(max_length=40, blank=True, null=True)
    consumer_password = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    number = models.CharField(max_length=12, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    security_question = models.CharField(max_length=255, blank=True, null=True)
    security_answer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consumer'


class ConsumerAnswerStatus(models.Model):
    consumer = models.ForeignKey(Consumer, models.DO_NOTHING, blank=True, null=True)
    question = models.ForeignKey('Question', models.DO_NOTHING, blank=True, null=True)
    testpaper = models.ForeignKey('Testpaper', models.DO_NOTHING, blank=True, null=True)
    questionbase = models.ForeignKey('Questionbase', models.DO_NOTHING, blank=True, null=True)
    answer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consumer_answer_status'


class ConsumerQuestionbase(models.Model):
    consumer = models.ForeignKey(Consumer, models.DO_NOTHING, blank=True, null=True)
    questionbase = models.ForeignKey('Questionbase', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consumer_questionbase'


class ConsumerTestpaper(models.Model):
    consumer = models.ForeignKey(Consumer, models.DO_NOTHING, blank=True, null=True)
    testpaper = models.ForeignKey('Testpaper', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consumer_testpaper'


class Gapfill(models.Model):
    question = models.ForeignKey('Question', models.DO_NOTHING, blank=True, null=True)
    standard_answer = models.CharField(max_length=255, blank=True, null=True)
    hard = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gapfill'


class Knowledge(models.Model):
    knowledge_id = models.BigAutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knowledge'


class Message(models.Model):
    message_of = models.ForeignKey(Consumer, models.DO_NOTHING, blank=True, null=True)
    message_out = models.ForeignKey(Consumer, models.DO_NOTHING, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class Question(models.Model):
    question_id = models.BigAutoField(primary_key=True)
    stems = models.TextField(blank=True, null=True)
    knowledge = models.ForeignKey(Knowledge, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'


class Questionbase(models.Model):
    questionbase_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questionbase'


class QuestionbaseQuestion(models.Model):
    questionbase = models.ForeignKey(Questionbase, models.DO_NOTHING, blank=True, null=True)
    question = models.ForeignKey(Question, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questionbase_question'


class Subject(models.Model):
    subject_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    knowledge = models.ForeignKey(Knowledge, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subject'


class Testpaper(models.Model):
    testpaper_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    apply_time = models.DateField(blank=True, null=True)
    subject = models.ForeignKey(Subject, models.DO_NOTHING, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    strats = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testpaper'


class TestpaperQuestion(models.Model):
    testpaper = models.ForeignKey(Testpaper, models.DO_NOTHING, blank=True, null=True)
    question = models.ForeignKey(Question, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testpaper_question'


class TrueOrFalse(models.Model):
    question = models.ForeignKey(Question, models.DO_NOTHING, blank=True, null=True)
    standard_answer = models.CharField(max_length=255, blank=True, null=True)
    hard = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'true_or_false'

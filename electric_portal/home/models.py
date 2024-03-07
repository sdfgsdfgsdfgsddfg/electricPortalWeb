from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
import bidi.algorithm

# Create your models here.

class UserTable(models.Model):
    main_user       = models.ForeignKey(User,on_delete=models.CASCADE)
    consultant_name = models.CharField(max_length=50)
    job_number      = models.CharField(max_length=50)
    phone           = models.CharField(max_length=13)
    user_role       = models.CharField(max_length=10)

    def __str__(self):
        return self.consultant_name

class Assay(models.Model):
    order_type      = models.BooleanField(default=True)
    assay_num       = models.CharField(max_length=50)
    mission_num     = models.CharField(max_length=50)
    permit_type     = models.CharField(max_length=50)
    contractor_name = models.CharField(max_length=50)
    feeder_num      = models.CharField(max_length=50)
    voltage_type    = models.CharField(max_length=20)
    location        = models.CharField(max_length=50)
    date            = models.CharField(max_length=20)
    user            = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    year            = models.CharField(max_length=5)
    month           = models.CharField(max_length=5)
    day             = models.CharField(max_length=5)

    def __str__(self):
        return self.assay_num


def create_image(size, bgColor, message, font, fontColor):
    W, H = size
    image = Image.new('RGB', size, bgColor)
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)-20, 20), message, font=font, fill=fontColor)
    return image

def create_image2(size, bgColor, message, font, fontColor,parent):
    W, H = size
    draw = ImageDraw.Draw(parent)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)-20, (H-h)-20), message, font=font, fill=fontColor)

def create_image3(size, bgColor, message, font, fontColor,parent):
    W, H = size
    draw = ImageDraw.Draw(parent)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)-20, (H-h)-50), message, font=font, fill=fontColor)

def create_image4(size, bgColor, message, font, fontColor,parent):
    W, H = size
    draw = ImageDraw.Draw(parent)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)-20, (H-h)-80), message, font=font, fill=fontColor)

class Permit(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    permit_img = models.ImageField(default='img/unknown.png' , upload_to="permits")
    location_ne = models.CharField(max_length=30)

    def updateImage(self, *args, **kwargs):
        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.permit_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class TeamModel(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    team_model_img = models.ImageField(default='img/unknown.png' , upload_to="team_model")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(TeamModel, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.team_model_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class PreworkMeeting(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    prework_meeting = models.ImageField(default='img/unknown.png' , upload_to="prework_meeting")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(PreworkMeeting, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.prework_meeting.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class RiskAssessment(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    risk_assessment_img = models.ImageField(default='img/unknown.png' , upload_to="risk_assessment")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(RiskAssessment, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.risk_assessment_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)


class SafeWorkProcedure(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    safe_work_procedures_img = models.ImageField(default='img/unknown.png' , upload_to="safe_work_procedures")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(SafeWorkProcedure, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.safe_work_procedures_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class Paramedic(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    paramedic_img = models.ImageField(default='img/unknown.png' , upload_to="paramedic")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(Paramedic, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.paramedic_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class Fighter(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    fighter = models.ImageField(default='img/unknown.png' , upload_to="fighter")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(Fighter, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.fighter.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class AssignedTask(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    assigned_task_img = models.ImageField(default='img/unknown.png' , upload_to="assigned_task")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(AssignedTask, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.assigned_task_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class ArtificialSecurityCard(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    artificial_security_card_img = models.ImageField(default='img/unknown.png' , upload_to="artificial_security_card")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(ArtificialSecurityCard, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.artificial_security_card_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class RecipientCard(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    recipient_card_img = models.ImageField(default='img/unknown.png' , upload_to="recipient_card")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(RecipientCard, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.recipient_card_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class SourceCard(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    source_card_img = models.ImageField(default='img/unknown.png' , upload_to="source_card")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(SourceCard, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.source_card_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class ResidenceCard(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    residence_img = models.ImageField(default='img/unknown.png' , upload_to="residence")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(ResidenceCard, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.residence_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class TUVForEquipmentAndDriver(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    TUV_for_equipment_and_driver_img  = models.ImageField(default='img/unknown.png' , upload_to="TUV_for_equipment_and_driver")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(TUVForEquipmentAndDriver, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.TUV_for_equipment_and_driver_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class FireExtinguisher(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    fire_extinguisher_img = models.ImageField(default='img/unknown.png' , upload_to="fire_extinguisher")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(FireExtinguisher, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.fire_extinguisher_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class FirstAid(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    first_aid_img = models.ImageField(default='img/unknown.png' , upload_to="first_aid")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(FirstAid, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.first_aid_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class WorkTeam(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    work_team_img = models.ImageField(default='img/unknown.png' , upload_to="work_team")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(WorkTeam, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.work_team_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class PicturesOfSite(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    pictures_of_site_img = models.ImageField(default='img/unknown.png' , upload_to="pictures_of_site")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(PicturesOfSite, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.pictures_of_site_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class SubscriptionNumber(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    subscription_number_img = models.ImageField(default='img/unknown.png' , upload_to="subscription_number")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(SubscriptionNumber, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.subscription_number_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class CutterCapacity(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    cutter_capacity_img = models.ImageField(default='img/unknown.png' , upload_to="cutter_capacity")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(CutterCapacity, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.cutter_capacity_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class MeterCapacity(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    meter_capacity_img = models.ImageField(default='img/unknown.png' , upload_to="meter_capacity")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(MeterCapacity, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.meter_capacity_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class DepthOfExcavation(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    depth_of_excavation_img = models.ImageField(default='img/unknown.png' , upload_to="depth_of_excavation")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(DepthOfExcavation, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.depth_of_excavation_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class FossilView(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    fossil_view_img = models.ImageField(default='img/unknown.png' , upload_to="fossil_view")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(FossilView, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.fossil_view_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class CableLength(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    cable_length_img = models.ImageField(default='img/unknown.png' , upload_to="cable_length")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(CableLength, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.cable_length_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class SafetyBarrier(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    safety_barriers_img = models.ImageField(default='img/unknown.png' , upload_to="safety_barriers")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(SafetyBarrier, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.safety_barriers_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class Object(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    object_img = models.ImageField(default='img/unknown.png' , upload_to="objects")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(Object, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.object_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class Obstacle(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    obstacles_img = models.ImageField(default='img/unknown.png' , upload_to="obstacles")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(Obstacle, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.obstacles_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class Violation(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    violations_img = models.ImageField(default='img/unknown.png' , upload_to="violations")
    location_ne = models.CharField(max_length=30)
    
    def updateImage(self, *args, **kwargs):
        super(Violation, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.location)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape(self.location_ne)
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.violations_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('./static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('./static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)
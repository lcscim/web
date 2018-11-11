#__author__:asus
#date:2018/11/11
import datetime
from django.contrib.contenttypes.models import ContentType
from .models import ReadNum,ReadDetail
from django.utils import timezone
from django.db.models import Sum

def read_statistics_once_read(request,obj):
    ct = ContentType.objects.get_for_model(obj)
    key = '%s_%s_read' % (ct.model,obj.pk)
    if not request.COOKIES.get(key):

        #方法二
        #总阅读数+1
        readnum,created = ReadNum.objects.get_or_create(content_type=ct,object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()
        #当天阅读数+1
        date = timezone.now().date()
        readDetail,created = ReadDetail.objects.get_or_create(content_type=ct,object_id=obj.pk,date=date)
        readDetail.read_num += 1
        readDetail.save()

    return key

def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    read_sums=[]
    dates = []
    for i in range(7,0,-1):
        date = today-datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_detail = ReadDetail.objects.filter(content_type=content_type,date=date)
        result = read_detail.aggregate(read_num_sum=Sum('read_num'))
        read_sums.append(result['read_num_sum'] or 0)
    return dates,read_sums
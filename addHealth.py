import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# driver=webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\chromedriver.exe')
driver = webdriver.Chrome()
driver.get("http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/index.do?t_s=1598842050761&amp_sec_version_=1&gid_=eEFadUJjQWRoNXZjcVBHNjRWZUhCcFI5d0RUdERPTVJVZGRlM3JlbnpoaHFvZ01pSUhuZ3pwYTB5Nm9QbkJ1Q0dsOTExOWRWWlRqMlNHY0NqVGxhREE9PQ&EMAP_LANG=zh&THEME=indigo#/dailyReport")
js_health = """
$('div[data-action="add"]').click();
var flag = false;

var interval = setInterval(() => {
    if(!flag && $('input[name="DZ_JSDTCJTW"]')) {
        flag = true;
        $('input[name="DZ_JSDTCJTW"]').val('36.3');
        $('#save').click();
        $('.bh-dialog-btnContainerBox').children()[0].click()
        clearInterval(interval);
    }
}, 3000);
"""
try:
#输入账户和密码

# user file

 driver.find_element_by_xpath("//*[@id='username']").send_keys("")
 driver.find_element_by_xpath("//*[@id='password']").send_keys("")
 print("输入账号成功")
 time.sleep(2)
#接着点击“登录”
 driver.find_element_by_xpath("//*[@id='casLoginForm']/p[5]/button").click()
 print("登录成功")
 time.sleep(5)
 
 driver.execute_script(js_health)
 print("打卡成功")
 time.sleep(7)
 driver.delete_all_cookies()
except:
 print("失败")




driver.get("http://ehall.seu.edu.cn/qljfwapp3/sys/lwWiseduElectronicPass/index.do?t_s=1598842055040&amp_sec_version_=1&gid_=eEFadUJjQWRoNXZjcVBHNjRWZUhCcFI5d0RUdERPTVJVZGRlM3JlbnpoaHFvZ01pSUhuZ3pwYTB5Nm9QbkJ1Q0dsOTExOWRWWlRqMlNHY0NqVGxhREE9PQ&EMAP_LANG=zh&THEME=indigo#/application")#seu
js_enther = """
$('div[data-action="add"]').click();
var flag = false;
Date.prototype.Format = function(fmt)   
{   
  var o = {   
    "M+" : this.getMonth()+1,                 //月份   
    "d+" : this.getDate(),                    //日   
    "h+" : this.getHours(),                   //小时   
    "m+" : this.getMinutes(),                 //分   
    "s+" : this.getSeconds(),                 //秒   
    "q+" : Math.floor((this.getMonth()+3)/3), //季度   
    "S"  : this.getMilliseconds()             //毫秒   
  };   
  if(/(y+)/.test(fmt))   
    fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));   
  for(var k in o)   
    if(new RegExp("("+ k +")").test(fmt))   
  fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));   
  return fmt;   
}

var interval = setInterval(() => {
    if(!flag && $('div[data-name="SFFHFHYQ"] .jqx-dropdownlist-content')) {

        flag = true;
        var curDate = new Date();
        var date = new Date((curDate/1000+86400)*1000);
        var dateformat = date.Format('yyyy-MM-dd')
        var dateStart = dateformat + " 08:51:00";
        var dateEnd = dateformat + " 21:51:00";

        $('div[data-name="SFFHFHYQ"] .jqx-dropdownlist-content').html('是');
        $('div[data-name="SFFHFHYQ"] input').val('1');

        $('div[data-name="NFZHGRFH"] .jqx-dropdownlist-content').html('是');
        $('div[data-name="NFZHGRFH"] input').val('1');

        $('div[data-name="SFYZNJJJGL"] .jqx-dropdownlist-content').html('是');
        $('div[data-name="SFYZNJJJGL"] input').val('1');

        $('div[data-name="DZ_JRSTZK"] .jqx-dropdownlist-content').html('是');
        $('div[data-name="DZ_JRSTZK"] input').val('1');

        $('div[data-name="CAMPUS"] .jqx-dropdownlist-content').html('<span unselectable="on">四牌楼-校区</span>');
        $('div[data-name="CAMPUS"] input').val('4');

        $('div[data-name="IN_SCHOOL_TIME"] input').val(dateStart);
        $('div[data-name="OFF_SCHOOL_TIME"] input').val(dateEnd);
        $('input[data-name="SDLY"]').val('图书馆');

        $('div[data-name="SQ_REASON"] .jqx-dropdownlist-content').html('到图书馆学习借书');
        $('div[data-name="SQ_REASON"] input').val('4');

        $('.ivu-btn-success').click();
        var timeout = setTimeout(() => {
            $('.bh-dialog-btnContainerBox').children()[0].click();
            clearTimeout(timeout)
        }, 1000);
        clearInterval(interval);
    }
}, 3000);
"""
try:
 time.sleep(5)
 driver.execute_script(js_enther)
 print("申请成功")
 time.sleep(7)
except:
 print("失败")

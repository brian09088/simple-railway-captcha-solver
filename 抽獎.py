from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 创建一个Firefox浏览器实例
driver = webdriver.Firefox()

# 開始答題 
driver.get("https://game.mnd.gov.tw/gameindex.aspx")

# 開始答題按鈕go
driver.find_element_by_class_name("img-fluid mt-sm-3").click()

# driver1 = webdriver.Firefox()
# driver1.get("https://game.mnd.gov.tw/gameplay.aspx")

# 模拟答题过程
for i in range(9):
    
    # 在这里编写代码模拟点击的操作
    # driver.find_element_by_class_name(' ').click()

    # 臺灣能擁有安全與穩定的環境，是因為什麼？
    if(driver.find_element_by_class_name('臺灣能擁有安全與穩定的環境，是因為什麼？')):
        driver.find_element_by_id("Ans4").click()

    # 全民國防教育的目的為何？
    if(driver.find_element_by_class_name('全民國防教育的目的為何？')):
        driver.find_element_by_id("Ans3").click()
        
    # 關於「漢光演習」以下何者正確？
    if(driver.find_element_by_class_name('關於「漢光演習」以下何者正確？')):
        driver.find_element_by_id("Ans1").click()
    
    # 守護家園是國軍的使命與責任，因應非傳統安全挑戰及民眾照護，國軍依行政院指導，配合各部會及地方政府，執行「」等任務，展現國軍「保護人民、守護家園」的具體行動？
    if(driver.find_element_by_class_name('守護家園是國軍的使命與責任，因應非傳統安全挑戰及民眾照護，國軍依行政院指導，配合各部會及地方政府，執行「」等任務，展現國軍「保護人民、守護家園」的具體行動？')):
        driver.find_element_by_id("Ans3").click()
    
    # 113年起1年期義務役在「入伍訓練」中，要學習的課程有？
    if(driver.find_element_by_class_name('113年起1年期義務役在「入伍訓練」中，要學習的課程有？')):
        driver.find_element_by_id("Ans4").click()

    # 為保障後備軍人接受召集之相關權益，於 111 年 5 月 27 日制定公布《後備軍人召集優待條例》，藉以達到廣儲後備能量及提升後備戰力之目標，以下何者為「非」？
    if(driver.find_element_by_class_name('為保障後備軍人接受召集之相關權益，於 111 年 5 月 27 日制定公布《後備軍人召集優待條例》，藉以達到廣儲後備能量及提升後備戰力之目標，以下何者為「非」？')):
        driver.find_element_by_id("Ans3").click()
    
    # 臺灣位處什麼樣的戰略位置，使臺海局勢變化牽動著國際交通線安全與經濟發展？
    if(driver.find_element_by_class_name('臺灣位處什麼樣的戰略位置，使臺海局勢變化牽動著國際交通線安全與經濟發展？')):
        driver.find_element_by_id("Ans1").click()

    # 我們位在政治體制區隔與地理位置最前緣，面對中共始終不放棄武力犯臺的實質威脅，國軍堅守之信念為何？
    if(driver.find_element_by_class_name('我們位在政治體制區隔與地理位置最前緣，面對中共始終不放棄武力犯臺的實質威脅，國軍堅守之信念為何？')):
        driver.find_element_by_id("Ans3").click()

    # 提升後備部隊基幹人力，與常備主戰部隊，構成堅強與持續之防禦體系之目標為何？
    if(driver.find_element_by_class_name('提升後備部隊基幹人力，與常備主戰部隊，構成堅強與持續之防禦體系之目標為何？')):
        driver.find_element_by_id("Ans1").click()

    # 確保人民生活日常，是國軍的責任，也是國軍存在的價值，以下何者是國軍秉持不變的態度？
    if(driver.find_element_by_class_name('確保人民生活日常，是國軍的責任，也是國軍存在的價值，以下何者是國軍秉持不變的態度？')):
        driver.find_element_by_id("Ans1").click()

    # 保國衛民為國軍核心任務，現階段我國防戰略目標包括？
    if(driver.find_element_by_class_name('保國衛民為國軍核心任務，現階段我國防戰略目標包括？')):
        driver.find_element_by_id("Ans3").click()

    # 目前正在籌建中的「」承接原國軍歷史文物館功能，呈現國軍光榮歷史與珍貴文物，以闡揚國軍建軍迄今「捍衛家園、保護人民」之貢獻？
    if(driver.find_element_by_class_name('目前正在籌建中的「」承接原國軍歷史文物館功能，呈現國軍光榮歷史與珍貴文物，以闡揚國軍建軍迄今「捍衛家園、保護人民」之貢獻？')):
        driver.find_element_by_id("Ans2").click()

    # 以下何者為我國防自主的成果？
    if(driver.find_element_by_class_name('以下何者為我國防自主的成果？')):
        driver.find_element_by_id("Ans4").click()

    # 為強化地方政府對戰爭發生時應變制變能力，111 年「」演習，首度結合戰時景況與災害救援想定，動員警、消、公（民）營事業、慈善機構與民間社團，有效驗證運用全民總力？
    if(driver.find_element_by_class_name('為強化地方政府對戰爭發生時應變制變能力，111 年「」演習，首度結合戰時景況與災害救援想定，動員警、消、公（民）營事業、慈善機構與民間社團，有效驗證運用全民總力？')):
        driver.find_element_by_id("Ans1").click()

    # 近年中共積極爭取區域內主導權，頻繁對我發動認知作戰、灰色地帶侵擾與軍事威懾行動，為何臺海安全情勢會成為全球關注焦點？
    if(driver.find_element_by_class_name('近年中共積極爭取區域內主導權，頻繁對我發動認知作戰、灰色地帶侵擾與軍事威懾行動，為何臺海安全情勢會成為全球關注焦點？')):
        driver.find_element_by_id("Ans2").click()

    # 全民國防教育的目的為何？
    if(driver.find_element_by_class_name('全民國防教育的目的為何？')):
        driver.find_element_by_id("Ans3").click()

    # 中共以灰色地帶手段改變臺海現狀，讓軍事壓迫襲擾成為「新常態」，國軍也相應推動國防施政，以下何者為「非」？
    if(driver.find_element_by_class_name('中共以灰色地帶手段改變臺海現狀，讓軍事壓迫襲擾成為「新常態」，國軍也相應推動國防施政，以下何者為「非」？')):
        driver.find_element_by_id("Ans1").click()
    
    # 為了紀念國軍在抗日戰爭中的英勇犧牲，以彰顯國軍守護國家的責任與榮耀，在1955年政府訂定「抗日戰爭勝利紀念日」為我國軍人節，是幾月幾日？
    if(driver.find_element_by_class_name('為了紀念國軍在抗日戰爭中的英勇犧牲，以彰顯國軍守護國家的責任與榮耀，在1955年政府訂定「抗日戰爭勝利紀念日」為我國軍人節，是幾月幾日？')):
        driver.find_element_by_id("Ans2").click()

    # 「一法、三公報、六項保證」是美「中」臺三邊關係的基礎，何者為六項保證之內容？
    if(driver.find_element_by_class_name('「一法、三公報、六項保證」是美「中」臺三邊關係的基礎，何者為六項保證之內容？')):
        driver.find_element_by_id("Ans4").click()
        
    # 為肆應未來戰場景況，14 天教召從原「在營區」報到及操課，改為結合「」報到、編成及施訓，並結合年度同心演習，依戰時分散部署位置，逐次驗證「連編成地」召訓？    
    if(driver.find_element_by_class_name('為肆應未來戰場景況，14 天教召從原「在營區」報到及操課，改為結合「」報到、編成及施訓，並結合年度同心演習，依戰時分散部署位置，逐次驗證「連編成地」召訓？')):
        driver.find_element_by_id("Ans2").click()
        
    # 為提升民眾對國防事務關注、支持及參與程度，國防部透過文宣製播、交流互動等作為，深化自我防衛共識，使國人堅定「」的信念與心理韌性？
    if(driver.find_element_by_class_name('為提升民眾對國防事務關注、支持及參與程度，國防部透過文宣製播、交流互動等作為，深化自我防衛共識，使國人堅定「」的信念與心理韌性？')):
        driver.find_element_by_id("Ans3").click()

    # 113年起1年期義務役在「部隊訓練」中，要學習的課程有？
    if(driver.find_element_by_class_name('113年起1年期義務役在「部隊訓練」中，要學習的課程有？')):
        driver.find_element_by_id("Ans4").click()
    
    # 全民國防教育區分為學校教育、政府機關（構）在職教育、社會教育及國防文物保護、宣導及教育等四大範疇，請問結合觀光資源推廣軍事遺跡或汰除裝備，屬哪一範疇？
    if(driver.find_element_by_class_name('全民國防教育區分為學校教育、政府機關（構）在職教育、社會教育及國防文物保護、宣導及教育等四大範疇，請問結合觀光資源推廣軍事遺跡或汰除裝備，屬哪一範疇？？')):
        driver.find_element_by_id("Ans2").click()

    # 為落實「全民關注、全民支持、全民參與」的全民國防理念，國防部與各部會、直轄市及縣（市）政府合作，策辦什麼活動，推廣全民國防？
    if(driver.find_element_by_class_name('為落實「全民關注、全民支持、全民參與」的全民國防理念，國防部與各部會、直轄市及縣（市）政府合作，策辦什麼活動，推廣全民國防？')):
        driver.find_element_by_id("Ans3").click()

    # 我國是目前世界上少數能夠全面性自主研發各類型飛彈的國家，以下何者為國產飛彈系列？
    if(driver.find_element_by_class_name('我國是目前世界上少數能夠全面性自主研發各類型飛彈的國家，以下何者為國產飛彈系列？')):
        driver.find_element_by_id("Ans4").click()

    # 為消弭假訊息對國軍官兵認知及士氣之影響，國防部加強各類不實、錯誤訊息蒐報，並採快速查證、即時回應及追查溯源等積極作為，提供國人正確資訊，以下何者為假訊息查證平臺？
    if(driver.find_element_by_class_name('為消弭假訊息對國軍官兵認知及士氣之影響，國防部加強各類不實、錯誤訊息蒐報，並採快速查證、即時回應及追查溯源等積極作為，提供國人正確資訊，以下何者為假訊息查證平臺？')):
        driver.find_element_by_id("Ans3").click()

    # 因應敵情威脅，未來我國整體國防，由哪些領域組成全民國防體系，分別依其任務屬性與責任區分，賦予保衛國家、守護家園與維持社會運作韌性的任務？
    if(driver.find_element_by_class_name('因應敵情威脅，未來我國整體國防，由哪些領域組成全民國防體系，分別依其任務屬性與責任區分，賦予保衛國家、守護家園與維持社會運作韌性的任務？')):
        driver.find_element_by_id("Ans2").click()
    
    # 以下何者為我國基本國防理念？
    if(driver.find_element_by_class_name('以下何者為我國基本國防理念？')):
        driver.find_element_by_id("Ans4").click()

    # 國防部以什麼方式擴大教育層面，將全民國防教育深化至各年齡層？
    if(driver.find_element_by_class_name('國防部以什麼方式擴大教育層面，將全民國防教育深化至各年齡層？')):
        driver.find_element_by_id("Ans1").click()
    
    # 海軍敦睦遠航訓練之目的為何？
    if(driver.find_element_by_class_name('海軍敦睦遠航訓練之目的為何？')):
        driver.find_element_by_id("Ans3").click()

    # 為提升部隊戰力、強化全民防衛與軍事動員能量，自113年1月1日起，94年1月1日以後出生之役男將服1年期之常備兵役，在入伍結訓後分發部隊服役，請問入伍訓是為期幾週的訓練？
    if(driver.find_element_by_class_name('為提升部隊戰力、強化全民防衛與軍事動員能量，自113年1月1日起，94年1月1日以後出生之役男將服1年期之常備兵役，在入伍結訓後分發部隊服役，請問入伍訓是為期幾週的訓練？')):
        driver.find_element_by_id("Ans1").click()
    
    # if(driver.find_element_by_class_name('')):
    # driver.find_element_by_id("Ans").click()

    # 暂停一段时间，以模拟用户阅读题目
    time.sleep(5)

# driver2 = webdriver.current_url()
# driver2.get("https://game.mnd.gov.tw/complete.aspx")

# 输入帐号和验证码
username = "B123382043"
code = "123456"  # 你需要通过其他方式获取验证码
driver.find_element_by_id('PID').send_keys(username)
driver.find_element_by_id('txtValidateCode').send_keys(code)

time.sleep(30)

# 模拟点击提交按钮-再玩一次
# driver3.get("https://game.mnd.gov.tw/completedOK.aspx")
# 回到gameindex頁面
driver.find_element_by_id('ImgBtn').click()

# 关闭浏览器
driver.quit()

# lipidiipikar (လိပိဒီပိကာ)
Lipidiipikar is the first telegraph code for Burmese (Myanmar language), invented by [Yaw Min Gyi U Pho Hlaing](https://my.wikipedia.org/wiki/%E1%80%98%E1%80%AD%E1%80%AF%E1%80%B8%E1%80%9C%E1%80%BE%E1%80%AD%E1%80%AF%E1%80%84%E1%80%BA%E1%81%8A_%E1%80%A6%E1%80%B8(%E1%80%9A%E1%80%B1%E1%80%AC%E1%80%99%E1%80%84%E1%80%BA%E1%80%B8%E1%80%80%E1%80%BC%E1%80%AE%E1%80%B8)) in 1869. I have developed a software simulation of this encoding based on two books: Lipidiipikar, written by Yaw Min Gyi U Pho Hlaing in 1869, and Myanmar Scientists of the Konbaung Period, written by Dr. Myo Thant Tin in 1984.

## Hacking Lipidiipikar Encoding

ယောမင်းကြီး ဦးဖိုးလှိုင်က ၁၈၆၉ ရေးသားခဲ့တဲ့ [လိပိဒီပိကာကျမ်း](https://github.com/ye-kyaw-thu/lipidiipikar/blob/main/references/lipidiipikar.pdf) စာအုပ်ကို CleanText ကုမ္ပဏီက စာပြန်ရိုက်ပြီး digitized လုပ်ထားတဲ့ စာအုပ်ကို အွန်လိုင်းကနေတဆင့် ဖတ်ဖူးခဲ့တာကတော့ နှစ်ပေါင်းတော်တော်ကြာခဲ့ပါပြီ။ ကွန်ပျူတာသမား တစ်ယောက်အနေနဲ့ကြည့်ရင် encoding method တစ်ခုမို့လို့ စိတ်ဝင်စားတာကော၊ မြန်မာစာကို ကြေးနန်းရိုက်လို့ရအောင် မြန်မာလူမျိုးပညာရှင်ကြီးတစ်ဦးဖြစ်တဲ့ ဦးဖိုးလှိုင်က ရေးသားခဲ့တဲ့ ပရိုပိုဇယ်လည်းဖြစ်တာကြောင့် encoding simulation ကို ဒီနှစ် ဩဂုတ်လလောက်ကတည်းက အချိန်ရရင် ရသလို စတင်ပြင်ဆင်ဖြစ်ခဲ့တယ်။ 

ခက်တာက လိပိဒီပိကာကျမ်း အပြင် မြန်မာ့ကြေးနန်းအကြောင်း ရေးသားထားတာက များများစားစား ရှိပုံမရဘူး။ ဦးဖိုးလှိုင်က အဲဒီကျမ်းစာအုပ်ထုတ်ဝေပြီး လအနည်းငယ် အကြာမှာပဲ အင်္ဂလိပ်သံအရာရှိ မက်မာဟွန်က အင်္ဂလိပ်ဘာသာသို့ပြန်ဆိုရေးသားခဲ့တယ် ဆိုတဲ့စာအုပ်ကိုလည်း ဖတ်ချင်လို့ ရှာဖွေနေတာ ခုချိန်ထိ ရှာလို့မတွေ့သေးပါဘူး။ အဲဒါနဲ့ PDF ဖိုင် စာမျက်နှာ ၁၆မျက်နှာခန့် ရှိတဲ့ လိပိဒီပိကာကျမ်း ထဲမှာ ရေးသားထားတာတွေကိုပဲ အခြေခံပြီး ပုံမှန်မြန်မာစာကြောင်းတွေကို conversion/encoding စမ်းလုပ်ကြည့်ခဲ့တယ်။ ဦးဖိုးလှိုင်ရဲ့ အိုက်ဒီယာက မြန်မာစာက အင်္ဂလိပ်စာနဲ့ မတူပဲ အကျဉ်းရေးနည်းနဲ့ အကျယ်ရေးနည်းဆိုပြီး စနစ်နှစ်မျိုးနဲ့ ရေးသားနိုင်တယ်။ အကျဉ်းရေးနည်းဆိုတာက လက်ရှိ ကျွန်တော်တို့ ရေးနေတဲ့၊ သုံးနေတဲ့စနစ်ကို ဆိုလိုတာပါ။ ဗျည်းနဲ့ သရတွဲတဲ့အခါမှာ အထူးပြုပြင်ထားတဲ့ သရ/ဗျည်း ပုံစံတွေဖြစ်တဲ့ ရေးချာ၊ မောက်ချာ၊ သဝေထိုး၊ ယပင်း၊ ရရစ်၊ ဝဆွဲ၊ ဟထိုး၊ လုံးကြီးတင်၊ တစ်ချောင်းငင် စတာတွေနဲ့ တွဲရေးတဲ့ ပုံစံပါ။ အဲဒီအကျဉ်းရေးနည်းကိုပဲ သုံးပြီး ကြေးနန်းမှာ ပို့ရင် သတ်မှတ်ရမယ့် ကုဒ်တွေက တအားများသွားနိုင်တယ်။ အဲဒါကြောင့် ဣ၊ ဤ၊ ဥ၊ ဦ၊ ဧ၊ ဩ စတဲ့ သရတွေကိုပဲသုံးပြီး ဗျည်းနဲ့တွဲရေးတဲ့ အကျယ်ရေးနည်းကိုသုံးသင့်တယ်။ ဒါ့အပြင် အသံတူတဲ့ ဗျည်းတွေကို ဖြုတ်တာမျိုး၊ အသုံးနည်းတဲ့ ဗျည်းတွေကို လျှော့တာမျိုး လုပ်ပြီး ရေးလို့ရလိမ့်မယ် ဆိုတာကို အဆိုပြုခဲ့တာပါ။  မြင်သာအောင် ဇယားတချို့နဲ့ ပြရရင်အောက်ပါ မြန်မာစာ ကြေးနန်းစနစ်အတွက်က အောက်ပါ စာလုံးတွေကိုပဲ အသုံးပြုမယ်လို့ ဆိုလိုပါတယ်။  

<div align="center">  
	
|<!-- -->|<!-- -->|<!-- -->|<!-- -->|  
| --- | --- | --- | --- |   
| က   | ခ   | ဂ   | င   |  
| စ   | ဆ   | ဇ   | ည   |  
| တ   | ထ   | ဒ   | န   |  
| ပ   | ဖ   | ဘ   | မ   |  
| ယ   | ရ   | လ   | ဝ   |  
| သ   | ဟ   |     |     |  
| အံ | အား | အ   |     |  

Table. လိပိဒီပိက မှာ သုံးတဲ့ ဗျည်း ၂၅လုံး   

|<!-- -->|<!-- -->|<!-- -->|<!-- -->|<!-- -->|<!-- -->|<!-- -->|<!-- -->|<!-- -->|<!-- -->|<!-- -->|<!-- -->|  
| --- | --- | --- | --- |--- | --- | --- | --- |--- | --- | --- | --- |   
|အကျဉ်းရေးနည်း |က |ကာ |ကိ |ကီ |ကု |ကူ |ကေ |ကဲ |ကော |ကော် |ကို|  
|အကျယ်ရေးနည်း |ကအ |ကအာ |ကဣ |ကဤ |ကဥ |ကဦ |ကဧ |ကဧဲ |ကဩ |ကဪ |ကအို|    

Table. ဗျည်းနှင့်သရ တွဲပုံနှစ်မျိုး 
</div>  

အဲဒီလို အကျယ်ရေးတဲ့အခါမှာ ဗျည်းတွေလည်းထပ်ဆင့်ကုန်တာမို့လို့ ဝဏ္ဏ (i.e. syllable) တစ်ခုစီခွဲရေးမှ ရပါလိမ့်မယ်။ ဒါ့အပြင် ဝဏ္ဏတစ်ခုမှာ ရေးတဲ့အစီအစဉ်အတိုင်းပဲ ချရေးသွားမှ အဆင်ပြေပါလိမ့်မယ်။ နားလည်ရလွယ်အောင် မြန်မာစာလုံး တချို့ကို ဥပမာပေးပြီး ဖြည့်စွက်ရှင်းပြရရင် အောက်ပါဇယားအတိုင်းပါ။    

<div align="center">  
	
|အကျဉ်းရေးနည်း |လိပိဒီပိကာ အကျယ်ရေးနည်း|  
|-----|-----|   
|လျှာ |လဟယအာ| လယဟအာ|  
|သည်းခံ| သအညး ခအံ|  
|မှန် |မဟအန|  
|မြှင့် |မဟရအင့|  
|ရှေး |ရဟဧး|  
|လိပိဒီပိကာ| လဣ ပဣ ဒဤ ပဣ ကအာ|  

Table. လိပိဒီပိကာ အကျယ်ရေးနည်း ဥပမာတချို့   
</div>  

လိပိဒီပိကာကျမ်းကို နှစ်ခေါက်လောက်ဖတ်လိုက်တဲ့အခါမှာ ဦးဖိုးလှိုင်ရဲ့ အကျယ်ပြောင်းရေးတဲ့ concept ကိုတော့ကောင်းကောင်း သဘောပေါက်ပါတယ်။ သို့သော် proof of concept (POC) လုပ်နိုင်ဖို့အတွက်ကျ ကျွန်တော့အနေနဲ့ ရှင်းရတဲ့ပြဿနာက နှစ်ခုပါ။ တစ်ခုက လက်ရှိသုံးနေကြတဲ့ ယူနီကုဒ်ကို အခြေခံတဲ့ မြန်မာစာလုံးအကုန်၊ စာကြောင်းအကုန်ကို ပြောင်းဖို့အတွက် rule ဘယ်လိုထုတ်ရမလဲ ဆိုတဲ့ အပိုင်းပါ။ ဒီကိစ္စကတော့ NLP R&D ကို တောက်လျှောက်လုပ်လာခဲ့တာမို့ ရှိထားတဲ့ အတွေ့အကြုံကနေ၊ test-data ပြင်ဆင်ပြီး coding လုပ်လိုက်၊ run ကြည့်ပြီး ထွက်လာတဲ့ output အမှားတွေကိုလေ့လာပြီး debug လုပ်လိုက်နဲ့ အချိန်ပေး ကြိုးစားသွားရင် အဆင်ပြေသွားလိမ့်မယ်လို့ နားလည်ထားပါတယ်။ နောက်ထပ် ရှင်းရမယ့် အပိုင်း၊ နားမလည်တဲ့အပိုင်းက အကျယ်စနစ်ကို ပြောင်းထားပြီးသား မြန်မာစာကြောင်းတွေကို လက်တွေ့မှာ ဘယ်လိုပုံစံမျိုးနဲ့ ကြေးနန်းပို့မှာလဲ၊ အခြေခံအားဖြင့် နားလည်ထားတဲ့ morse code အဖြစ်ဘယ်လို mapping လုပ်ရမလဲဆိုတာကို တိတိကျကျဖော်ပြထားချင်း မရှိတဲ့အပိုင်းပါ။ 

**အခု ဒီစာကို ဖတ်နေတဲ့ မိတ်ဆွေ၊ ကျောင်းသား၊ ကျောင်းသူတွေလည်း မသိသေးတဲ့ သမိုင်းကြောင်းကို ကိုယ်တိုင် ဖော်ထုတ်ရတာ၊ hacking လုပ်ရတာကို ဝါသနာပါရင် [လိပိဒီပိကကျမ်း](https://github.com/ye-kyaw-thu/lipidiipikar/blob/main/references/lipidiipikar.pdf)ကိုပဲ ဖတ်ပြီး ဘယ်လိုလက်တွေ့မှာ ကြေးနန်းပို့မှာလည်း ဆိုတဲ့ အပိုင်းကို စဉ်းစားကြည့်ကြပါလို့။(အဖြေက အခုဖတ်နေတဲ့ README ရဲ့ နောက်ဆုံးပိုင်းမှာ ရေးထားတာမို့လို့ အဲဒီအထိ မဖတ်ပဲ reference ဖိုလ်ဒါအောက်က lipidiipikar.pdf ဖိုင်ကိုပဲ ဖတ်ကြည့်ပါ)** 

တကယ်က ယောမင်းကြီးဦးဖိုးလှိုင်က သူ့ကျမ်းရဲ့ နိဂုံးအပိုင်းမှာ အောက်ပါအတိုင်း ရှင်းပြထားပါတယ်။    
(လိပိဒီပိကာ ကျမ်းမှာ စာပိုဒ် တစ်ခုချင်းစီကို နံပါတ်တပ်ရေးထားပါတယ်။ စုစုပေါင်း စာပိုဒ် ၇၀ပါရှိပါတယ်။)    

-----  

၆၄။ ဤအကျယ် ရေးနည်း၌ အရစ်၊ အပင့်၊ လုံးကြီးတင်၊ တချောင်းငယ်၊ အစရှိသော ဗျည်းနှင့် ကပ်သည့် သရပုံ အထူးမရှိသော့ကြောင့် သက်သက်သော သရရေးပုံနှင့် ဗျည်းရေးပုံတို့ကို ဆိုခဲ့ပြီးသော နည်းဖြင့် ရှေ့နောက်အစီအစဉ်အတိုင်း ရေးထားလျှင်ပင် အလိုရှိသော စကားဖြစ်နိုင်သည်။ ထို့ကြောင့် စကားပြော ဓာတ်အိုး၏ မျက်နှာပြင်တွင် ရေးသားထားသော သရပုံ၊ ဗျည်းပုံတို့ကို ဓာတ်အိုး၌ တန်းသော သံနန်းဖြင့် ဓာတ်၏ သတ္တိအားဖြင့် ထိခိုက်၍ အိမ်မြှောင်တည့်ရာ ဗျည်း၊ သရတို့ကို ယူ၍ ရေးလျှင် အလိုရှိသော စကား အကျယ် ရေးနည်းအတိုင်း ဖြစ်၏။  

၆၅။ မီးမျိုးစုံ၊ အလံမျိုးစုံတို့ဖြင့် စကားပြောရာ၌လည်း သရ၊ ဗျည်းတို့အဖို့ လုံးရေစေ့အောင် မီးမျိုး၊ အလံမျိုး ပြုလုပ်ထားလျှင် အလိုရှိရာ စကားကို ပြောဆိုနိုင်သည်။ စကားပြောနန်း ဓာတ်အိုး မျက်နှာတွင် သရပုံ၊ ဗျည်းပုံတထပ်၊ ဂဏန်းပုံတထပ်၊ နှစ်ထပ်၊ ဝန်းဝိုင်း၍ ရေးလျက်ရှိသော့ကြောင့် အိမ်မြှောင် တည့်သည်ကာလ၊ ဗျည်းပုံ၊ သရပုံနှင့်တကွ ဂဏန်းမှာလည်း အိမ်မြှောင်ခေါင်း တည့်သောကြောင့် စာလုံးပုံနှင့် ဂဏန်းပုံ မည်သည်ကို ယူရမည် မသိနိုင်ရန် ရှိ၍ ပဌမ သတိပေး ခေါင်းလောင်း ထိုးပြီးနောက် စကားကို ပြောမည်ဖြစ်လျှင် စာလုံးမှာ အိမ်မြှောင်ခေါင်းကို တည့်စေပြီးမှ အလိုရှိရာ စကားကို ပြောနိုင်သည်။ ဂဏန်းကို ပြောလိုလျှင် ဂငယ် စာလုံးပုံတွင် အိမ်မြှောင်ခေါင်းကို တည့်စေပြီးမှ အလိုရှိရာ ဂဏန်းကို ပြောနိုင်သည်။ ပုဒ်မကို အလိုရှိလျှင် ဓာတ်အိုး မျက်နှာပြင်တွင် ပါသော အလံပုံတွင် အိမ်မြှောင် တည့်စေရမည်။   

၆၆။ ဤသို့ ဆိုခဲ့ပြီးသော နည်းအတိုင်း တန်းလုပ်တော်မူသော စကားပြောနန်း၌ အမှတ်အသားထား၍ ပြောဆိုနိုင်ကုန်၏။   

၆၇။ မီးဖြူ၊ မီးဝါ အစရှိသော မီးမျိုးစုံတို့ဖြင့်၎င်း၊ အလံမျိုးစုံတို့ဖြင့်၎င်း စကားပြောရာ၌ ဤဓာတ်အိုး နန်းတို့ဖြင့် စကားပြောဆို နှိုင်သကဲ့သို့ အမှတ်အသားထား၍ ပြောဆို နိုင်ကုန်၏။   

၆၈။ စကားပြောရန် ဓာတ်အိုး လုပ်ဆောင်ခြင်းသည်လည်း အမျိုးမျိုး ရှိကုန်၏။ အချို့ ဓာတ်အိုး၌ တီးခတ်သော အချက်ဖြင့် စာလုံးကို မှတ်ကုန်၏။ အချို့ဓာတ်အိုးစာလုံး ဟူ၍ အမှတ်သညာ ပေးသော အရေးအဆွဲးတို့ဖြင့် လုပ်ဆောင်ကုန်၏။ အချို့ဓာတ်အိုး၌ သံလိုက်ကို အိမ်မြှောင်ကဲ့သို့ထား၍ လုပ်ဆောင်ကုန်၏။   

၆၉။ ဤသို့ အစရှိသည်ဖြင့် အထူးထူး အထွေထွေ လုပ်ဆောင်ကြငြားသော်လည်း ယခုအခါ နိုင်ငံတော်တွင် အဦးအစ၊ ပဌမ ဖြစ်သော့ကြောင့် သိသာ ထင်ရှားလွယ်အောင် ဓာတ်အိုး မျက်နှာပြင်၌ စာလုံးပုံထား၍ အိမ်မြှောင်နှင့် တည့်စေသော ဓာတ်အိုးဖြင့် လုပ်ဆောင်စေတော်မူ၏။  

၇၀။ ဤသို့ ဆိုခဲ့ပြီးသော စကားတို့ဖြင့် ကျီအတွင်းဝန်၊ ယောမြို့စားမင်း၊ မင်းကြီးမင်းလှ မဟာစည်သူသည် အက္ခရာ ပုံသဏ္ဌာန်တို့၏ ရေးသားနည်းကို ခပ်သိမ်းသော သူတို့ အလွယ်တကူ သိစေခြင်းငှာ စီရင်အပ်သော လိပိဒီပိကာ မည်သောကျမ်းသည် သက္ကရာဇ် ၁၂၃၁ခု၊ တပို့တွဲးလဆန်း ၁၅ရက်နေ့ အပြီးသို့ ရောက်၏။ 

-----  

အဲဒီ စာပိုဒ် ၆၄ ကနေ ၇၀ အထိကို အကြိမ်ကြိမ်အခါခါဖတ်လည်း ကျွန်တော့အနေနဲ့ကတော့ ရေးထားတဲ့ ဓာတ်အိုး၊ နန်း၊ အိမ်မြှောင် ဆိုတဲ့ စက်ပစ္စည်းအပိုင်းတွေနဲ့ ပတ်သက်ပြီး မမြင်နိုင်ခဲ့ပါဘူး။ အဲဒါနဲ့ အလုပ်အားတဲ့အချိန်တွေမှာ ကြေးနန်း (telegraph) နဲ့ဆိုင်တာတွေ၊ လက်လှမ်းမီတဲ့ ဆက်သွယ်ရေး သမိုင်းစာအုပ်တွေ၊ အပြည်ပြည်ဆိုင်ရာ morse code စံသတ်မှတ်ချက်တွေ၊ website တွေကို မွှေနှောက်ရှာဖွေရင်း၊ တချို့ လူကြီးတွေ၊ မိတ်ဆွေတွေကိုလည်း တိုင်ပင်ကြည့်ရင်း အဖြေအတိအကျမရပဲ တစ်လကျော်၊ နှစ်လနည်းပါး သောင်တင်နေခဲ့ပါတယ်။ ဦးဖိုးလှိုင်တို့ မြန်မာလိုကြေးနန်း စပို့နိုင်ဖို့ encoding အပိုင်းရော၊ ဆက်သွယ်ရေး တိုင်ထောင်တာတွေလုပ်ဖို့ စီစဉ်နေတဲ့အချိန်အခါဆိုတာက မြန်မာပြည်အောက်ပိုင်းကို အင်္ဂလိပ်ကသိမ်းပြီး ကိုလိုနီလုပ်ထားတဲ့အချိန်မို့လို့ အိန္ဒိယနိုင်ငံရဲ့ ကြေးနန်းဆက်သွယ်ရေး သမိုင်းတွေ၊ စာအုပ်အဟောင်းတွေကိုလည်း ရှာဖတ်ရင်း လမ်းစကို ရှာလို့ မရခဲ့ပါဘူး...  

တကယ်က ကျွန်တော်က Global Information and Telecommunication ဆိုတဲ့ ဘာသာရပ်နဲ့ ဂျပန်နိုင်ငံ ဝါဆဲဒတက္ကသိုလ်မှာ မဟာဘွဲ့၊ ဒေါက်တာဘွဲ့ ယူခဲ့တာမို့လို့ ဆက်သွယ်ရေးအင်ဂျင်နီယာ (communication engineering) နဲ့ ပတ်သက်တဲ့ ပညာရပ်တချို့ကို သင်ကြားဖူးခဲ့ပါတယ်။ သို့သော်လည်း ကုန်းဘောင်ခေတ်ပတ်ဝန်းကျင် ၁၈ရာစုလောက်က သုံးခဲ့ကြတဲ့ hardware တွေနဲ့ electrical telegraph machine တွေနဲ့ ပတ်သက်ပြီး မသင်ခဲ့ရ၊ မရင်းနှီးခဲ့တာက အမှန်ပါပဲ။ ဒီလိုနဲ့ ၂၀၂၄ စက်တင်ဘာ၊ အောက်တာဘာလအတွင်းမှာ ဟိုရောက်ဒီရောက်နဲ့ ရှာဖွေလေ့လာဖြစ်သွားပြီး အင်တာနက် အွန်လိုင်းပြတိုက်တချို့ရဲ့ website တွေကနေ ၁၈၅၀ ပတ်ဝန်းကျင်က အသုံးပြုခဲ့ကြတဲ့ ကြေးနန်းစက်တွေနည်း ပတ်သက်ပြီး တော်တော်လေး တီးမိခေါက်မိရှိလာပါတယ်။ အဲဒါနဲ့ အောက်ပါ စက်သုံးမျိုးထဲက တစ်မျိုးတော့ ဖြစ်လိမ့်မယ်။ မြန်မာမှာ ပထမဆုံး ကြေးနန်းပို့ဖို့အတွက် သုံးခဲ့တဲ့စက်က ABC machine ဖြစ်ဖို့ များတယ်လို့ ခန့်မှန်းမိခဲ့ပါတယ်။ 

<p align="center">
<img src="https://github.com/ye-kyaw-thu/lipidiipikar/blob/main/pic/1280px-Wallace_Study-Telegraph.jpg" alt="" width="330"/>  
<img src="https://github.com/ye-kyaw-thu/lipidiipikar/blob/main/pic/five-needle-telegraph-machine-from-PowerHouse-Collections.png" alt="Five Neddle Telegraph Machine" width="300"/>
<img src="https://github.com/ye-kyaw-thu/lipidiipikar/blob/main/pic/ABC_machine-wiki.jpg" alt="ABC Machine" width="230"/>
</p>  
<div align="center">
  Fig. Left: Morse Key, Center: Cooke and Wheatstone five niddle telegraph, Right: ABC Machine  
</div> 

<br />

သို့သော်လည်း ဘယ်စက်ကို သုံးခဲ့တယ် ဆိုတာကို ပုံနဲ့တကွရှိရင်၊ ဒါမှမဟုတ်ရင်လည်း ဘုံနာမည်နဲ့ မဟုတ်ပဲ စက်ကိုထုတ်တဲ့ ကုမ္ပဏီနာမည်နဲ့တကွ ရေးထားတဲ့ စာအုပ်၊ စာတမ်း၊ ကျမ်းရှိကောင်း ရှိနိုင်တယ်ဆိုပြီး မြန်မာလိုရေးထားတဲ့ ကုန်းဘောင်ခေတ်၊ ကိုလိုနီခေတ်သမိုင်းကြောင်းစာအုပ်တွေ၊ ဦးဖိုးလှိုင်၊ ကနောင်မင်းသားတို့နဲ့ ပတ်သက်တဲ့ စာအုပ်တွေကို ဟိုရှာဒီရှာလုပ်ရင်းနဲ့ ဒေါက်တာမျိုးသန့်တင် ရေးသားထားတဲ့ "ကုန်းဘောင်ခေတ် မြန်မာ့သိပ္ပံပညာရှင်များ" ဆိုတဲ့ စာအုပ်အကြောင်းကို သိလာလို့ LU Lab. ကတပည့်တွေဆီကို လှမ်းအကြောင်းကြားတော့ နာရီပိုင်းအတွင်းမှာပါပဲ မောင်သူရအောင် (KMITL Univ., Thailand) ဆီကနေ စကန်ဖတ်ထားတဲ့ pdf ဖိုင်ကို ပို့ပေးလို့ ဖတ်လိုက်တော့ စာမျက်နှာ ၆၄ မှာ ရေးထားတဲ့ ["ကုန်းဘောင်ခေတ် မြန်မာ့ကြေးနန်း"](https://github.com/ye-kyaw-thu/lipidiipikar/blob/main/references/Myanmar-Scientist-of-KongBaung-2to7-64to81.pdf) ဆိုတဲ့ အခန်းကို ဖတ်လိုက်တော့မှပဲ တောက်လျှောက်ရှာဖွေနေတဲ့ အချက်အလက်အတိအကျ သို့မဟုတ် အဖြေကို ရရှိခဲ့ပါတယ်။ အောက်ပါ ပုံကိုတွေ့တော့ အရမ်းကို ဝမ်းသာခဲ့ရပါတယ်။ တကယ်တမ်းက ရေးဆွဲထားတာက ကုန်းဘောင်ခေတ်မှာ သုံးခဲ့ကြတဲ့ ကြေးနန်းစက်နဲ့ ဘယ်လောက်အထိ အတိအကျတူသလဲ မသေချာပေမဲ့ ဒီပုံ (i.e. mapping) က ကျွန်တော်လုပ်နေတဲ့ lipidiipika simulation အလုပ်အတွက် တန်ဖိုးမဖြတ်နိုင်တဲ့ အချက်အလက်မို့ အဲဒီနေ့ကတော့ တကယ့် အမှတ်တရပါပဲ။ ရက်စွဲအတဲအကျ က 24 Oct 2024 မှာပါ။ သူရအောင်ကိုလည်း ကျေးဇူးတင်တယ်။  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/lipidiipikar/blob/main/pic/my-kyaenan-dial.png" alt="Myanmar KyaeNan Dial" width="450"/>  
</p>  
<div align="center">
  Fig. ရှေးခေတ် မြန်မာ့ကြေးနန်း ဒိုင်ခွက် (ABC machine နဲ့တွဲသုံးခဲ့ဟု ယူဆ)  
</div> 



## Usage Information

You can get usage information by running the script with the --help option.  

```
$ python ./lipi.py --help
usage: lipi.py [-h] [--input INPUT] [--output OUTPUT]

Myanmar Text Processor

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        Input filename
  --output OUTPUT, -o OUTPUT
                        Output filename
```

The following is an example text from the original Lipidiipikar book:  

စကားပြောနန်းတန်းလုပ်စေသူစာရေးကြီးအသုံးစာရေးတို့စကားပြောနန်းတန်းရန်လမ်းတွင်တိုင်စိုက်လုပ်ရန်မှစ၍အရပ်ရပ်လုပ်ဆောင်ရန်ရှိသည်များကို၁၂၃၁ခုနှစ်အတွင်းပြီးပြေအောင်လုပ်ဆောင်ကြရမည်ခတ်လှေအဆန်တွင်လည်းမည်ရွေ့မည်မျှလုပ်ဆောင်ပြီးပြေသည်များကိုမပြတ်တင်လျှောက်လိုက်ရမည်။  


For encoding the raw1.txt file, run the following command:  

```
python ./lipi.py --input ./raw1.txt --output ./raw1.lipi
```

The encoded content will be as follows:  

စအ ကအား ပရဩ နအနး တအနး လဥပ စဧ သဦ စအာ ရဧး ကရဤး အ သဥံး စအာ ရဧး တအို့ စအ ကအား ပရဩ နအနး တအနး ရအန လအမး တဝအင တအိုင စအိုက လဥပ ရအန မဟအ စအ ရဝဧ့ အ ရအပ ရအပ လဥပ ဆဩင ရအန ရဟဣ သအည မယအား ကအို ၁ ၂ ၃ ၁ ခဥ နဟအစ အ တဝအငး ပရဤး ပရဧ ဩင လဥပ ဆဩင ကရအ ရအ မအည ခအတ လဟဧ အ ဆအန တဝအင လအညး မအည ရဝဧ့ မအည မယဟအ လဥပ ဆဩင ပရဤး ပရဧ သအည မယအား ကအို မအ ပရအတ တအင လယဟဩက လအိုက ရအ မအည  


## GUI Information  

If you want to run the program with a GUI, ensure that the "index.html" file is located in the templates folder. Run the following command in your terminal:

```
python lipi-gui.py
```

Copy and paste the generated HTTP link (e.g., http://127.0.0.1:5000) into your web browser.   
You will see the following Lipidiipikar GUI simulation in your browser.  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/lipidiipikar/blob/main/pic/lipidiipikar-gui-ver1.0.png" alt="lipidiipikar-gui-ver1.0.png" width="600"/>  
</p>  
<div align="center">
  Fig. GUI of Lipidiipikar encoding simulation (lipi-gui.py)  
</div> 

## License 

Ye Kyaw Thu, LU Lab Leader, released the Lipidiipikar simulation code under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by-nc/4.0/) license.  

Please refer to the [LICENSE.txt](https://github.com/ye-kyaw-thu/lipidiipikar/blob/main/LICENSE.txt) file.  

## Citation

If you want to use Lipidiipikar in your research, I would appreciate it if you use the following reference:  

```
@misc{ye2024lipidiipikar,
	author = {Ye Kyaw Thu},
	title = {Hacking Lipidiipikar},
	howpublished = {https://github.com/ye-kyaw-thu/lipidiipikar},
	year = {2024}
}
```

## Further Studies

1. Consider adding detailed options, such as using "ဂ" (ga) for transmitting Myanmar numbers, or incorporating a "flag" to indicate the end of a sentence.
2. Test with text from social media and entries from the Pali dictionary.
3. Implement decoding functionality to revert back to normal text.

## References

1. Electrical Telegraph, [https://en.wikipedia.org/wiki/Electrical_telegraph](https://en.wikipedia.org/wiki/Electrical_telegraph)
2. လိပိဒီပိကာကျမ်း၊ ယောအတွင်းဝန် ဦးဖိုးလှိုင်၊ ၁၈၆၉၊ typed/digitized by CleanText, [lipidiipikar.pdf](https://github.com/ye-kyaw-thu/lipidiipikar/blob/main/references/lipidiipikar.pdf)
3. ကုန်းဘော်ခေတ် မြန်မာ့သိပ္ပံပညာရှင်များ၊ ဒေါက်တာမျိုးသန့်တင်၊ စာပေလောက သုတစာအုပ်အမှတ် ၁၅၃၊ စာပေလောက စာအုပ်တိုက်၊ ဒီဇင်ဘာ ၁၉၈၄
4. [The Unicode Standard, Version 16.0](https://www.unicode.org/charts/PDF/U1000.pdf)
5. [မြန်မာသင်ပုန်းကြီး](https://my.wikipedia.org/wiki/%E1%80%99%E1%80%BC%E1%80%94%E1%80%BA%E1%80%99%E1%80%AC%E1%80%9E%E1%80%84%E1%80%BA%E1%80%95%E1%80%AF%E1%80%94%E1%80%BA%E1%80%B8%E1%80%80%E1%80%BC%E1%80%AE%E1%80%B8)
6. [Wiki page of Yaw Min Gyi U Phoe Hlaing (ယောမင်းကြီး ဦးဘိုးလှိုင်)](https://my.wikipedia.org/wiki/%E1%80%98%E1%80%AD%E1%80%AF%E1%80%B8%E1%80%9C%E1%80%BE%E1%80%AD%E1%80%AF%E1%80%84%E1%80%BA%E1%81%8A_%E1%80%A6%E1%80%B8(%E1%80%9A%E1%80%B1%E1%80%AC%E1%80%99%E1%80%84%E1%80%BA%E1%80%B8%E1%80%80%E1%80%BC%E1%80%AE%E1%80%B8))
7. [Needle_telegraph, Wiki](https://en.wikipedia.org/wiki/Needle_telegraph)
8. [Morse code, Wiki](https://en.wikipedia.org/wiki/Morse_code)

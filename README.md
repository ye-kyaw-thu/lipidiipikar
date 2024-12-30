# lipidiipikar (လိပိဒီပိကာ)
Lipidiipikar is the first telegraph code for Burmese (Myanmar language), invented by Yaw Min Gyi U Pho Hlaing in 1869. I have developed a software simulation of this encoding based on two books: Lipidiipikar, written by Yaw Min Gyi U Pho Hlaing in 1869, and Myanmar Scientists of the Konbaung Period, written by Dr. Myo Thant Tin in 1984.

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

## References

1. Electrical Telegraph, [https://en.wikipedia.org/wiki/Electrical_telegraph](https://en.wikipedia.org/wiki/Electrical_telegraph)
2. လိပိဒီပိကာကျမ်း၊ ယောအတွင်းဝန် ဦးဖိုးလှိုင်၊ ၁၈၆၉၊ typed/digitized by CleanText, [lipidiipikar.pdf](https://github.com/ye-kyaw-thu/lipidiipikar/blob/main/references/lipidiipikar.pdf)
3. ကုန်းဘော်ခေတ် မြန်မာ့သိပ္ပံပညာရှင်များ၊ ဒေါက်တာမျိုးသန့်တင်၊ စာပေလောက သုတစာအုပ်အမှတ် ၁၅၃၊ စာပေလောက စာအုပ်တိုက်၊ ဒီဇင်ဘာ ၁၉၈၄
4. [The Unicode Standard, Version 16.0](https://www.unicode.org/charts/PDF/U1000.pdf)
5. [မြန်မာသင်ပုန်းကြီး](https://my.wikipedia.org/wiki/%E1%80%99%E1%80%BC%E1%80%94%E1%80%BA%E1%80%99%E1%80%AC%E1%80%9E%E1%80%84%E1%80%BA%E1%80%95%E1%80%AF%E1%80%94%E1%80%BA%E1%80%B8%E1%80%80%E1%80%BC%E1%80%AE%E1%80%B8)
6. [Wiki page of Yaw Min Gyi U Phoe Hlaing (ယောမင်းကြီး ဦးဘိုးလှိုင်)](https://my.wikipedia.org/wiki/%E1%80%98%E1%80%AD%E1%80%AF%E1%80%B8%E1%80%9C%E1%80%BE%E1%80%AD%E1%80%AF%E1%80%84%E1%80%BA%E1%81%8A_%E1%80%A6%E1%80%B8(%E1%80%9A%E1%80%B1%E1%80%AC%E1%80%99%E1%80%84%E1%80%BA%E1%80%B8%E1%80%80%E1%80%BC%E1%80%AE%E1%80%B8))

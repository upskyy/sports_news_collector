# Sports-News-Collector
- Sports-News-Collector collects sports news and offers several services.  
- It is provided using various models provided by [Pororo](https://github.com/kakaobrain/pororo).  



## Installation
```
pip install sports_news_collector
```  
## Usage
- After the import, you can check the events currently supported by the `sports_news_collector` through the following commands  
```python
>>> from sports_news_collector import SportsNewsCollector
>>> SportsNewsCollector.available_events()
['kbaseball', 'wbaseball', 'kfootball', 'wfootball', 'basketball', 'volleyball', 'golf', 'general', 'esports']
```  
- If you want to collect news from a specific event, you can put the event name in the `event` argument    
```python
>>> from sports_news_collector import SportsNewsCollector
>>> collector = SportsNewsCollector(event='wfootball')
```  
- After creating the object, you can use it like this:  
```python
>>> collector.collect()
```   

- Then, it is sent to your e-mail through the following procedure.  
-- 1.  Collect the news of the sport you have chosen.  
-- 2.  Summarize the news and analyze the sentiment of the news.  
-- 3.  Send them to your email periodically  
  
- If you want to send to your email periodically, I recommend using the colab environment.  
- Please click [here](https://github.com/hasangchun/sports_news_collector/blob/main/make_sports_news.ipynb) for details.  


## Information
![sports_news](https://user-images.githubusercontent.com/54731898/113507570-5fc78680-9586-11eb-8de1-5982f6f4c0c2.jpg)   
I got news information by crawling the recommended news of Naver Sports News.  


## Result
#### 1. Korea Baseball
![kbaseball](https://user-images.githubusercontent.com/54731898/113506464-065c5900-9580-11eb-8497-e85b370b10f1.jpg)  
  
#### 2. World Baseball
![wbaseball](https://user-images.githubusercontent.com/54731898/113506579-a2866000-9580-11eb-8b32-6041a3349c73.PNG)  

#### 3. Korea football
![kfootball](https://user-images.githubusercontent.com/54731898/113506882-4de3e480-9582-11eb-9dc6-c854db3039d7.PNG)  

#### 4. World football
![wfootball_](https://user-images.githubusercontent.com/54731898/113507444-6dc8d780-9585-11eb-9201-6939d43522b2.PNG)  
 

#### 5. Basketball
![basketball](https://user-images.githubusercontent.com/54731898/113507024-0b6ed780-9583-11eb-8ab8-36f59292eb62.PNG)  

#### 6. Volleyball
![volleyball](https://user-images.githubusercontent.com/54731898/113507088-6b657e00-9583-11eb-9b7e-be57918a0901.PNG)  

#### 7. Golf
![golf](https://user-images.githubusercontent.com/54731898/113507223-2726ad80-9584-11eb-8563-b4921f9eecc7.PNG)  

#### 8. General
 ![general](https://user-images.githubusercontent.com/54731898/113507260-576e4c00-9584-11eb-8fc6-bd1564d9e2df.PNG)  
 
#### 9. Esports
![esport](https://user-images.githubusercontent.com/54731898/113506466-06f4ef80-9580-11eb-9c06-e7f9ee2a5156.PNG)  


## Reference
- [pororo](https://kakaobrain.github.io/pororo/)  
- [myeonghak/stock-news-summary](https://github.com/myeonghak/stock-news-summary)  
- 
## License
```
Copyright 2021 Sangchun Ha.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

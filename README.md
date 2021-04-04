# Sports-News-Collector
---
- Sports-News-Collector collects sports news and offers several services.  
- It is provided using various models provided by [Pororo](https://github.com/kakaobrain/pororo).


  
## Installation
---
`pip install sports_news_collector`
  
    
## Usage
---
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
    
    
- Please click [here] for details.  

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
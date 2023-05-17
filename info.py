from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@sparta.mw5zmbb.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


doc = {'name':'김재혁',
       'MBTI':"ENFJ",
       'image':"https://files.slack.com/files-tmb/T043597JK8V-F057YHRBX34-dc65e23c6b/capture2_720.png",
       'strength':"뒤쳐지는 팀원이 없도록 꼼꼼히 잘 이끌어 나갑니다!",
       'reason':""
       }

db.info.insert_one(doc)


doc = {'name':'배병일',
       'MBTI':"INFP",
       'image':"https://ca.slack-edge.com/T043597JK8V-U056JF99DKJ-676687d724d8-48",
       'strength':"생각 한 바가 있으면 적극적으로 어필해 잘 이해시킬 수 있습니다!",
       'reason':"학창 시절 게임을 즐겨 했고 핵을 쓰는 유저를 보면서 부러워했습니다. 나는 이렇게 노력하는데 쟤네들은 편하게 게임하면서 더 쌔지는구나..라는 생각이 들었고 매크로,핵을 인터넷에서 찾아 내가 쓰고 싶은 쪽으로 조금씩 수정하여 사용하니 아주 재미있었습니다. 그 당시에는 이게 뭔지도 몰랐고 그냥 게임을 편하게 하기 위해서 사용했던 것 인데 시간이 지나고 내가 뭘 재밌어했는지 돌이켜보니 코드를 수정하면서 내가 원하는 대로 수정했던 학생때가 생각이 났고 시간이 빠르게 지나갔던 기억이 났습니다.  코딩에 대해 알아보다 스파르타코딩클럽을 알게 되었고 새로운 도전을 하기 위해 지원하게 되었습니다."
       }
db.info.insert_one(doc)


doc = {'name':'장두혁',
       'MBTI':"ENTP",
       'image':"https://res.cloudinary.com/dyhnnmhcf/image/upload/v1681745025/profileImage_ny0a9b.jpg",
       'strength':"경쟁심을 원동력으로 삼아 누구보다 빠르게 성장 합니다! ",
       'reason':""
       }
db.info.insert_one(doc)

doc = {'name':'오준석',
       'MBTI':"INFP",
       'strength':"여러 의견을 귀 기울여 들을 줄 아는 세심한 프로소통러가 바로 접니다!",
       'image':"https://i.ibb.co/XtCX6d8/ojs.jpg",
       'reason':"개발자에 대한 로망이 있었고, 지금이 아니면 앞으로 좋은 기회가 없을 거 같아 참여하게 되었습니다.코딩을 하여 결과물을 만드는 과정이 예전부터 흥미롭다는 생각을 늘 했습니다. 이전에 개발 회사에 재직했던 경험 또한 개인적으로 좋은 경험이라 앞으로 직업을 갖는다면 개발자가 되고 싶다고 여겨 선택하게 되었습니다.모두 파이팅입니다!"}

db.info.insert_one(doc)

doc = {'name':'조윤주',
       'MBTI':"INFP",
       'image':"https://i.ibb.co/3y6gpvz/Kakao-Talk-20230515-154815213.jpg",
       'strength':"스스로의 능력 밖 부분은 빠르게 인정하고 모르는 걸 질문하는 것을 주저하지 않습니다!",
       'reason':"CSS와 HTML만을 이용해 가상의 사이트를 만드는 작업을 해본 경험이 있었습니다,오류가 생기고 찾아내는 과정 , 모르는 것이 있으면 여러 사람들과 의사소통 하며 도움을 받고 , 또 반대의 상황에선 내가 도움을 주는 그런 일련의 과정들이 매력적으로 다가왔습니다.직장을 그만 두고 쉬는 과정에서 새로운 도전을 해보고 싶었습니다. 해서 이전의 경험을 토대로 내일배움 캠프에 지원하게 되었습니다!"
       }
db.info.insert_one(doc)
from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs" / "projects" / "lueshiji" / "iter-01"


SERIAL_PLAN = {
    "title": "略施计",
    "format": "serialized-comic",
    "format_route": "paged-comic",
    "total_chapters": 30,
    "default_target_pages": 20,
    "adaptation_premise": "一个被虐待的五岁女孩靠狗洞逃命、误闯疯父纪霆舟的湖心亭后，开始一点点夺回“被承认的资格”，并把原本注定继续腐烂的纪家改造成真正的家。",
    "series_engine": "黑色幽默父女修复 + 镜像双女儿关系 + 豪门旧案与药剂线外压",
    "audience_promise": "每一话都给出孩子视角的危险、荒诞和情感推进，并持续兑现父女关系改写与双女儿并肩成长的奖励。",
    "arcs": [
        {"arc": 1, "name": "Arc 1 - 狗洞与湖心亭", "chapter_start": 1, "chapter_end": 5, "goal": "让纪念活下来并闯进纪霆舟视野", "promise": "危险、黑色幽默、错认父亲", "major_turn": "沈清棠即将入府"},
        {"arc": 2, "name": "Arc 2 - 两个女儿", "chapter_start": 6, "chapter_end": 10, "goal": "让新妹妹入局，建立纪家的双女儿格局", "promise": "餐桌张力、旧伤暴露、位置争夺", "major_turn": "纪念先活住再抢回资格"},
        {"arc": 3, "name": "Arc 3 - 守密与试探", "chapter_start": 11, "chapter_end": 15, "goal": "把家住热，把药线和陈默线种下去", "promise": "结盟、守密、成人威胁逼近", "major_turn": "陈默不再只是远处的危险"},
        {"arc": 4, "name": "Arc 4 - 学校与流言", "chapter_start": 16, "chapter_end": 20, "goal": "把家庭冲突外翻到学校和公众空间", "promise": "外部舆论、身份冲突、公开护女", "major_turn": "纪霆舟开始公开选边"},
        {"arc": 5, "name": "Arc 5 - 旧案翻面", "chapter_start": 21, "chapter_end": 25, "goal": "把陈默、药剂、身世、旧账真正并线", "promise": "真相、站队、亲缘回收", "major_turn": "所有成人都被逼到表态"},
        {"arc": 6, "name": "Arc 6 - 正门回环", "chapter_start": 26, "chapter_end": 30, "goal": "把返村、长辈、旧照、烟花与全家站队收口", "promise": "情感兑现、家庭成型、首尾回环", "major_turn": "从狗洞逃命走到正门回家"},
    ],
    "chapters": [
        {"chapter": 1, "arc": 1, "title": "狗洞", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["开篇", "第1章", "第2章"], "core_goal": "让纪念从被追打到闯出旧院", "chapter_reward": "读者迅速认下纪念这张脸和这股野劲", "opening_hook": "被鞭子追着跑的小女孩和脑内系统同时开口", "page_turns": ["p5-狗洞位置暴露", "p11-湖心亭里坐着的男人", "p17-哥哥你真好看"], "ending_hook": "点心被扔进湖里，纪念终于意识到这个漂亮哥哥不是善茬", "focus_characters": ["纪念", "纪霆舟"], "visual_motif": "狗洞、鞭子、湖心亭逆光", "anchor_prop": "落湖点心", "notes": "整话必须以孩子视角压低成人的威压"},
        {"chapter": 2, "arc": 1, "title": "点心落湖", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第2章", "第3章", "第4章"], "core_goal": "把纪霆舟的危险和纪念的厚脸皮锁住", "chapter_reward": "父女第一次真正对话并建立荒诞关系", "opening_hook": "纪念求吃的，纪霆舟故意把点心扔进湖里", "page_turns": ["p4-系统提醒这人就是渣爹", "p10-纪霆舟第一次正眼看她", "p16-纪念赖着不走"], "ending_hook": "纪霆舟把她带回自己的生活区域", "focus_characters": ["纪念", "纪霆舟"], "visual_motif": "湖面、逆光、孩子仰头", "anchor_prop": "糕点盘", "notes": "把危险和喜感同时成立"},
        {"chapter": 3, "arc": 1, "title": "发烧夜", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第11章", "第12章", "第13章"], "core_goal": "让纪霆舟第一次在照料与厌恶间失守", "chapter_reward": "父女关系从观察转向身体上的接近", "opening_hook": "纪念发烧后死抓纪霆舟衣角不放", "page_turns": ["p6-纪霆舟差点把孩子丢出去", "p11-小孩梦中找爹", "p18-他还是把人抱稳了"], "ending_hook": "纪霆舟意识到自己正在记住她的名字", "focus_characters": ["纪念", "纪霆舟"], "visual_motif": "冷色房间、发红眼尾、抓袖子的手", "anchor_prop": "药和退烧毛巾", "notes": "这一话需要明显的静与慢"},
        {"chapter": 4, "arc": 1, "title": "新衣服和旧伤", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第14章", "第15章", "第16章"], "core_goal": "让纪念从旧院余孽转向被看见的孩子", "chapter_reward": "外形变化带来位置变化", "opening_hook": "纪念被量尺寸、被换上新衣服", "page_turns": ["p5-旧伤痕露出来", "p12-纪霆舟沉默看着", "p18-纪念主动试探新规则"], "ending_hook": "家里的人开始重新给纪念定位", "focus_characters": ["纪念", "纪霆舟", "知了"], "visual_motif": "软尺、卷发、新旧衣服对比", "anchor_prop": "量衣软尺", "notes": "把身体痕迹和生活升级并置"},
        {"chapter": 5, "arc": 1, "title": "新妹妹进门", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第17章", "第18章", "第19章", "第20章"], "core_goal": "让沈清棠入局并打破原书预设", "chapter_reward": "读者看到双女儿关系不是低配宫斗", "opening_hook": "系统提醒原书里女主进门后原主会更惨", "page_turns": ["p7-沈清棠真正出现", "p13-纪念没有按原书出招", "p18-餐桌站位第一次改变"], "ending_hook": "纪家正式变成三方拉扯场", "focus_characters": ["纪念", "沈清棠", "纪霆舟"], "visual_motif": "门厅、长桌、两个孩子的视线", "anchor_prop": "书包和糖纸", "notes": "两女儿初见要更复杂，不要工具化"},
        {"chapter": 6, "arc": 2, "title": "灵堂长桌", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第21章", "第22章", "第23章", "第24章"], "core_goal": "把纪家的家庭气压变成具体桌面戏", "chapter_reward": "纪霆舟第一次有了偏向纪念的身体动作", "opening_hook": "一顿饭吃得像审判", "page_turns": ["p5-魏杨记起旧日恩情", "p12-纪霆舟下意识先护纪念", "p19-沈清棠也看懂了变化"], "ending_hook": "家里开始有人不安地意识到纪念不会再回旧院", "focus_characters": ["纪念", "纪霆舟", "沈清棠", "魏杨"], "visual_motif": "长桌、筷子、视线交锋", "anchor_prop": "饭碗", "notes": "家庭关系要靠动作，不靠说教"},
        {"chapter": 7, "arc": 2, "title": "旧伤不会自己好", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第25章", "第26章", "第27章", "第28章", "第29章"], "core_goal": "把虐待后遗症拉回台面", "chapter_reward": "纪念的求生聪明第一次带来反击", "opening_hook": "纪念蹲在暗处看别人被抓", "page_turns": ["p6-她发现危险还在家里", "p13-纪霆舟察觉异常", "p18-孩子没有像原书那样自毁"], "ending_hook": "纪家里有人开始真正怕这个小孩活下来", "focus_characters": ["纪念", "纪霆舟", "旧院人"], "visual_motif": "暗处、抓痕、门缝", "anchor_prop": "药盒", "notes": "恐惧感要落到空间里"},
        {"chapter": 8, "arc": 2, "title": "狗、药和睡眠债", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第30章", "第31章", "第32章", "第33章", "第34章"], "core_goal": "把家住热，同时埋药剂线", "chapter_reward": "生活温度和危险线第一次同框", "opening_hook": "纪霆舟明明困得要死，却还是先看纪念", "page_turns": ["p4-狗先认了纪念", "p10-纪念用前世知识试药", "p17-知了看见不该看见的东西"], "ending_hook": "药线被一个大人模糊地闻到了", "focus_characters": ["纪念", "纪霆舟", "知了", "大蛋"], "visual_motif": "狗毛、药纸、困倦父亲", "anchor_prop": "药包", "notes": "温度不能盖掉危机"},
        {"chapter": 9, "arc": 2, "title": "谁在盯这个孩子", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第35章", "第36章", "第37章", "第38章", "第39章"], "core_goal": "把外部视线真正引入庄园", "chapter_reward": "读者明确知道危险不只来自家里", "opening_hook": "纪念觉得有人在盯自己", "page_turns": ["p5-纪霆舟先一步察觉", "p11-沈清棠不再只是被动旁观", "p18-陈默这条线第一次有具体形"], "ending_hook": "有人决定查纪念", "focus_characters": ["纪念", "沈清棠", "纪霆舟", "陈默"], "visual_motif": "窗、影子、病色", "anchor_prop": "旧照片", "notes": "陈默初登场要兼具病感和锋利"},
        {"chapter": 10, "arc": 2, "title": "先把这口气活下来", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第40章", "第41章", "第42章", "第43章", "第44章", "第45章", "第46章", "第47章", "第48章", "第49章", "第50章"], "core_goal": "给前 50 章一个阶段收束", "chapter_reward": "纪念先在纪家真正站住脚", "opening_hook": "纪念第一次明白自己不是只争一顿饭", "page_turns": ["p5-她开始主动抢规则", "p12-纪霆舟在公开场合偏向她", "p19-沈清棠选择站在她这边"], "ending_hook": "阶段性站稳，但更大的外压也被招来了", "focus_characters": ["纪念", "纪霆舟", "沈清棠"], "visual_motif": "门口站位、孩子抬眼、被改写的规矩", "anchor_prop": "门禁与药纸", "notes": "前 50 章的具体改编以这一话收束"},
        {"chapter": 11, "arc": 3, "title": "家里开始偏心", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第51章-第56章"], "core_goal": "把家庭秩序变化做实", "chapter_reward": "纪霆舟的偏爱第一次形成公共事实", "opening_hook": "一个原本没人会替纪念做的小动作被人做了", "page_turns": ["p8", "p14"], "ending_hook": "有人开始真正恨她", "focus_characters": ["纪念", "纪霆舟", "沈清棠"], "visual_motif": "夹菜、挡门、抱起", "anchor_prop": "儿童药", "notes": ""},
        {"chapter": 12, "arc": 3, "title": "两个女儿第一次结盟", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第57章-第62章"], "core_goal": "让双女儿关系从互看走向并肩", "chapter_reward": "读者看到沈清棠不是工具对手", "opening_hook": "沈清棠第一次替纪念遮一下", "page_turns": ["p7", "p15"], "ending_hook": "她们有了共同秘密", "focus_characters": ["纪念", "沈清棠"], "visual_motif": "两个孩子并肩", "anchor_prop": "糖纸", "notes": ""},
        {"chapter": 13, "arc": 3, "title": "魏杨和知了的站队", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第63章-第68章"], "core_goal": "把家庭支柱的立场写清", "chapter_reward": "家的温度变得可靠", "opening_hook": "大人们第一次不再隔岸看纪念", "page_turns": ["p6", "p14"], "ending_hook": "纪念的影响力超出她自己想象", "focus_characters": ["魏杨", "知了", "纪念"], "visual_motif": "围裙、文件夹、夜灯", "anchor_prop": "毛毯", "notes": ""},
        {"chapter": 14, "arc": 3, "title": "药方和秘密交换", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第69章-第74章"], "core_goal": "让药线转为主动戏", "chapter_reward": "纪念的能力开始真正改变局面", "opening_hook": "一张药方引出两种动机", "page_turns": ["p5", "p13"], "ending_hook": "秘密开始有成本", "focus_characters": ["纪念", "知了", "纪霆舟"], "visual_motif": "药纸、灯下手影", "anchor_prop": "药方", "notes": ""},
        {"chapter": 15, "arc": 3, "title": "陈默第一次咬上来", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第75章-第80章"], "core_goal": "让陈默线正式进主引擎", "chapter_reward": "危险终于有脸", "opening_hook": "病床上的人忽然精准说中纪念的异常", "page_turns": ["p7", "p16"], "ending_hook": "陈默决定继续查", "focus_characters": ["陈默", "纪念"], "visual_motif": "白床单、冷眼、血点", "anchor_prop": "礼盒", "notes": ""},
        {"chapter": 16, "arc": 4, "title": "规则被孩子改写", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第81章-第86章"], "core_goal": "进入学校前先改写家庭规则", "chapter_reward": "纪念从被适应的人变成定义规则的人", "opening_hook": "一条原本专门折磨孩子的规矩被她反拿来用", "page_turns": ["p8", "p14"], "ending_hook": "外部世界要来了", "focus_characters": ["纪念", "纪霆舟"], "visual_motif": "台阶、门框、坐席", "anchor_prop": "门禁卡", "notes": ""},
        {"chapter": 17, "arc": 4, "title": "学校门口的第一仗", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第87章-第92章"], "core_goal": "让家庭冲突外翻到学校", "chapter_reward": "主角在公共空间也不再后退", "opening_hook": "第一次站到校门口，纪念就被人盯上", "page_turns": ["p6", "p15"], "ending_hook": "她得学会在别人的规矩里反击", "focus_characters": ["纪念", "沈清棠"], "visual_motif": "校门、徽章、台阶", "anchor_prop": "书包", "notes": ""},
        {"chapter": 18, "arc": 4, "title": "谣言是另一种鞭子", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第93章-第98章"], "core_goal": "让舆论变成具体外压", "chapter_reward": "孩子第一次学会用别人的话反打别人", "opening_hook": "流言比鞭子更快", "page_turns": ["p7", "p13"], "ending_hook": "纪霆舟知道后不会再装看不见", "focus_characters": ["纪念", "纪霆舟"], "visual_motif": "纸条、走廊、围观圈", "anchor_prop": "传纸", "notes": ""},
        {"chapter": 19, "arc": 4, "title": "旧案影子回庄园", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第99章-第104章"], "core_goal": "把外部案件感带回家", "chapter_reward": "庄园不再只是家，也是现场", "opening_hook": "一张旧照把时间撕开", "page_turns": ["p6", "p14"], "ending_hook": "过去的人要回来算账", "focus_characters": ["陈默", "纪霆舟"], "visual_motif": "旧照、档案袋、暗走廊", "anchor_prop": "照片", "notes": ""},
        {"chapter": 20, "arc": 4, "title": "纪霆舟第一次公开护女", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第105章-第110章"], "core_goal": "让纪霆舟从私下护持转为公开站队", "chapter_reward": "观众拿到最爽的关系奖励", "opening_hook": "他在人前挡到纪念前面", "page_turns": ["p8", "p16"], "ending_hook": "再也不能回到‘假装不认’那一格", "focus_characters": ["纪霆舟", "纪念"], "visual_motif": "挡住视线的背影", "anchor_prop": "外套", "notes": ""},
        {"chapter": 21, "arc": 5, "title": "亲缘和收养都要算账", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第111章-第118章"], "core_goal": "把亲女/养女的价值冲突复杂化", "chapter_reward": "谁是家人不再靠血统一句话定夺", "opening_hook": "一句‘亲生的’并没解决问题", "page_turns": ["p7", "p14"], "ending_hook": "两种亲缘都要被重新定义", "focus_characters": ["纪念", "沈清棠", "纪霆舟"], "visual_motif": "两个孩子一左一右", "anchor_prop": "合照框", "notes": ""},
        {"chapter": 22, "arc": 5, "title": "陈默不是单纯敌人", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第119章-第126章"], "core_goal": "把陈默从敌人推进到复杂亲属", "chapter_reward": "旧案线有了情感厚度", "opening_hook": "陈默做了一件不像敌人的事", "page_turns": ["p5", "p15"], "ending_hook": "他必须选边", "focus_characters": ["陈默", "纪念"], "visual_motif": "停在门口的人", "anchor_prop": "病历夹", "notes": ""},
        {"chapter": 23, "arc": 5, "title": "两个女儿一起撒网", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第127章-第134章"], "core_goal": "让双女儿主动出手", "chapter_reward": "双女主真正成立", "opening_hook": "沈清棠和纪念决定一起钓人", "page_turns": ["p8", "p14"], "ending_hook": "对手开始低估两个孩子", "focus_characters": ["纪念", "沈清棠"], "visual_motif": "并肩的背影", "anchor_prop": "纸条和小礼物", "notes": ""},
        {"chapter": 24, "arc": 5, "title": "药剂线彻底翻面", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第135章-第142章"], "core_goal": "把药剂线从影子线变成正面战场", "chapter_reward": "之前所有药纸都开始回收", "opening_hook": "一包药让旧伤全开", "page_turns": ["p7", "p15"], "ending_hook": "再不公开就晚了", "focus_characters": ["纪念", "陈默", "纪霆舟"], "visual_motif": "药纸、玻璃杯、冷灯", "anchor_prop": "药瓶", "notes": ""},
        {"chapter": 25, "arc": 5, "title": "该选边的人都得选边", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第143章-第150章"], "core_goal": "把所有大人逼到站队", "chapter_reward": "家庭与旧案真正并轨", "opening_hook": "孩子已经没有躲的位置", "page_turns": ["p6", "p16"], "ending_hook": "纪家要去面对外面的长辈与村路了", "focus_characters": ["纪霆舟", "陈默", "知了", "魏杨"], "visual_motif": "门口集合", "anchor_prop": "车钥匙", "notes": ""},
        {"chapter": 26, "arc": 6, "title": "家不是遗产是站队", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第151章-第158章"], "core_goal": "给终局前的价值判断定调", "chapter_reward": "家这个词第一次不是虚词", "opening_hook": "有人把‘家’当财产，有人把它当人", "page_turns": ["p7", "p14"], "ending_hook": "返村路开始", "focus_characters": ["纪念", "纪霆舟"], "visual_motif": "门、钥匙、背影", "anchor_prop": "旧钥匙", "notes": ""},
        {"chapter": 27, "arc": 6, "title": "返村之前先过心关", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第159章-第166章"], "core_goal": "让终局不是单纯办事，而是先过情关", "chapter_reward": "纪霆舟终于学会面对活人", "opening_hook": "返村这件事把所有旧伤都翻出来了", "page_turns": ["p8", "p15"], "ending_hook": "车开出去就不能回头装没发生过", "focus_characters": ["纪念", "纪霆舟", "沈清棠"], "visual_motif": "车窗、夜路、沉默", "anchor_prop": "旧玩具", "notes": ""},
        {"chapter": 28, "arc": 6, "title": "外公外婆与旧照片", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第167章-第174章"], "core_goal": "让村路和长辈完成情感回收", "chapter_reward": "纪念终于接到祖辈的情感", "opening_hook": "一张旧照片比任何解释都重", "page_turns": ["p5", "p13"], "ending_hook": "所有关系开始朝合照站位移动", "focus_characters": ["纪念", "外公外婆", "纪霆舟"], "visual_motif": "老屋、鸡、旧照片", "anchor_prop": "合照", "notes": ""},
        {"chapter": 29, "arc": 6, "title": "正门回环", "target_pages": 20, "format_route": "paged-comic", "source_chapters": ["第175章-第180章"], "core_goal": "把狗洞和正门做成回环", "chapter_reward": "首尾呼应带来最强的结构满足", "opening_hook": "当年从狗洞逃出去的孩子，这次要从正门进", "page_turns": ["p8", "p17"], "ending_hook": "家终于轮到她来定义", "focus_characters": ["纪念", "纪霆舟"], "visual_motif": "狗洞、正门", "anchor_prop": "门锁", "notes": ""},
        {"chapter": 30, "arc": 6, "title": "烟花、合照、活着回家", "target_pages": 22, "format_route": "paged-comic", "source_chapters": ["第181章-第186章"], "core_goal": "收回‘活下来’这条最初行动脊柱", "chapter_reward": "荒诞和温情同时落地", "opening_hook": "烟花夜前的一张全家合照位置还空着", "page_turns": ["p9", "p18"], "ending_hook": "终章不是句号，而是家真正开始的那一晚", "focus_characters": ["纪念", "纪霆舟", "沈清棠", "陈默"], "visual_motif": "烟花、全家合照、门前光", "anchor_prop": "相机", "notes": ""},
    ],
}


def ensure(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).strip() + "\n", encoding="utf-8")


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    ensure(OUT)
    ensure(OUT / "样章长稿")
    ensure(OUT / "分页脚本")
    ensure(OUT / "分格脚本")

    write_text(
        OUT / "原作漫画改编诊断.md",
        """
        # 原作漫画改编诊断

        ## 项目

        - 原作：`略施计，懂爱后渣爹刀拿不稳了`
        - 本轮改编目标：做一部 `paged-comic` 连载漫画，全文 30 话规划，具体改编先落前 50 个源章节左右
        - 类型判断：黑色幽默 / 父女修复 / 镜像双女儿 / 豪门旧案

        ## 一句话前提

        一个靠狗洞逃命的五岁女孩误闯想让纪家血脉断绝的疯父生活，从“被遗忘的孩子”一路抢回被承认、被偏爱和被公开站队的资格。

        ## 为什么适合改漫画

        - 开篇就有强视觉事件：追打、狗洞、湖心亭、点心落湖
        - 孩子主角 + 成人威压非常适合用高度差、门框、桌沿和长腿制造画面压迫
        - 黑色幽默密度高，适合用夸张表情和停顿格做节奏
        - 纪霆舟危险又漂亮，天然具备大格和封面吸力
        - 沈清棠不是单纯对手，双女儿关系适合做并列构图和镜像页面
        - 药剂与旧案线能在中后段提供真实外压，不会只有家庭撒糖

        ## 必留元素

        - 狗洞逃命
        - 湖心亭认错“哥哥”
        - 点心落湖
        - 发烧夜抓袖口
        - 新衣服与旧伤并置
        - 沈清棠入府后的错位温柔
        - 长桌家庭戏
        - 陈默病色与锋利并存的出场感
        - 村路、旧照、鸡、烟花、全家合照

        ## 必压缩部分

        - 单纯重复“纪念很聪明”的校园证明段
        - 不改变关系温度的团宠证明段
        - 技术细节过密但戏剧变化很少的药剂说明段
        - 后段重复站队而不推进真相的桥段

        ## 漫画版引擎判断

        这部作品不能改成“甜宠儿童版”，也不能改成“旧案说明书”。

        最适合的漫画引擎是：

        - 前段：危险又好笑的父女生存战
        - 中段：双女儿成形 + 庄园住热 + 秘密守护
        - 后段：旧案翻面 + 所有人站队 + 正门回环

        ## 风险

        1. 如果把黑色幽默洗得太干净，纪念会失去最强记忆点。
        2. 如果把漫画页面写成影视分镜，孩子视角优势会被浪费。
        3. 如果陈默和药剂线写得比人物关系更复杂，会压垮可读性。
        4. 如果沈清棠被工具化，整部作品会掉到低级争宠模板。
        """,
    )

    write_text(
        OUT / "漫画总圣经.md",
        """
        # 漫画总圣经

        ## 形式

        - 形态：`paged-comic`
        - 话数：30 话
        - 每话目标：20 页左右
        - 阅读承诺：每一话都给出明确奖励和页尾追更理由

        ## Logline

        五岁女孩纪念靠狗洞逃出旧院，误闯疯父纪霆舟的湖心亭后，本该继续被遗忘的人生彻底偏轨。她一边在纪家抢回位置，一边改写即将进门的养女、暗中查探的病弱对手、以及纪家几代人留下的旧伤，最终把“活下来”一步步活成“真正回家”。

        ## 改编前提

        家不是别人施舍给你的地方，而是你一次次用偏爱、站队和公开选择抢回来的位置。

        ## 观众承诺

        - 前 2 话锁狗洞、湖心亭、点心落湖
        - 前 5 话锁住双女儿将入局的张力
        - 前 10 话让纪念先在纪家活住并站住
        - 中段持续交付“家住热了，但危险变具体了”
        - 终段必须完成狗洞到正门的回环

        ## 六段结构

        - Arc 1：狗洞与湖心亭
        - Arc 2：两个女儿
        - Arc 3：守密与试探
        - Arc 4：学校与流言
        - Arc 5：旧案翻面
        - Arc 6：正门回环

        ## 页面母题

        - 高度差：孩子视角看成人腿、桌沿、门把、楼梯
        - 门与阈限：狗洞、房门、正门、病房门、车门
        - 吃与药：点心、药纸、药瓶、喂食、添菜
        - 手势：抓袖子、按桌子、递出去又收回来
        - 光：湖心亭逆光、卧室夜灯、病房冷光、烟花夜
        """,
    )

    write_text(
        OUT / "人物设定圣经.md",
        """
        # 人物设定圣经

        ## 纪念

        - 年龄感：五岁身体，成年人灵魂
        - 外形：乱卷长发、细瘦、小小一只但眼神不怕人
        - 表情主轴：嘴硬、抬眼、突然发亮、装可怜、憋笑
        - 动作主轴：抓、钻、扑、蹲、踮脚、抠、突然站直
        - 视觉关键词：狗洞、药纸、脏衣服换新衣、抓袖口

        ## 纪霆舟

        - 观感：漂亮、瘦、危险、困、随时可能翻脸
        - 眼睛：墨绿里带血丝，压迫感强
        - 动作主轴：垂眼、突然伸手、挡、抱起、拎开、停住
        - 视觉关键词：湖心亭、伤手、长桌、夜色、抱孩子时的别扭

        ## 沈清棠

        - 观感：乖、清秀、看着像标准答案，但骨子里也很早熟
        - 动作主轴：背书包、轻拽衣角、停顿后站过去、压住脾气
        - 视觉关键词：书包带、糖纸、作文、安静站位

        ## 陈默

        - 观感：病色、冷白、眼神像刀，情绪很少但每次都不白给
        - 动作主轴：咳、停、看、把礼盒放下、不进门只站门口
        - 视觉关键词：病床、白床单血点、礼盒、旧照片

        ## 魏杨 / 知了

        - 不是工具人
        - 他们负责把纪家从“设定”变成“生活空间”
        - 一个偏执行与人情，一个偏生活与守护
        """,
    )

    write_text(
        OUT / "场景道具圣经.md",
        """
        # 场景道具圣经

        ## 关键场景

        ### 旧院与狗洞楼梯
        - 作用：开篇生存压迫
        - 关键词：楼梯、破椅子、鞭子、狗洞、草丛

        ### 湖心亭
        - 作用：纪念与纪霆舟第一次真正相遇
        - 关键词：逆光、水面、点心盘、长腿、冷脸

        ### 纪霆舟卧房
        - 作用：发烧夜、睡眠债、父女关系变位
        - 关键词：夜灯、床沿、毛巾、药、被抓皱的衣袖

        ### 长桌餐厅
        - 作用：家庭秩序可视化
        - 关键词：座位、碗筷、谁给谁夹菜、谁先坐下

        ### 门厅 / 校门 / 病房门
        - 作用：阈限空间，人物关系是否跨过去

        ### 村路与老屋
        - 作用：终局情感回收
        - 关键词：旧照片、鸡、烟花、门前空地

        ## 关键道具

        - 点心：最早的羞辱与诱惑
        - 药纸 / 药瓶：危险线和修复线共用
        - 旧照片：旧案和亲缘回收
        - 书包：沈清棠的秩序感
        - 礼盒：陈默的试探式善意
        - 门锁 / 正门：首尾回环
        """,
    )

    write_json(OUT / "连载规划.json", SERIAL_PLAN)

    write_text(
        OUT / "连续性账本.md",
        """
        # 连续性账本

        ## 时间

        - 起点：纪念穿进书中当天
        - 第 1 话：旧院逃命 -> 湖心亭
        - 第 2-4 话：被纪霆舟正式纳入可见范围
        - 第 5 话：沈清棠入府
        - 第 10 话：前 50 章改编阶段性收束，纪念在纪家站住脚

        ## 秘密归属

        - 纪念知道：自己穿书、原书部分走向、沈清棠将入府
        - 纪霆舟知道：纪念是自己的亲生女儿，但最初并不想承认
        - 沈清棠最早知道：纪家很冷、纪念和原书设定不一样
        - 陈默最早知道：纪念有异常，值得查

        ## 关系温度

        - 纪念 -> 纪霆舟：从“漂亮疯哥哥”到“危险渣爹”到“可以赌一把的人”
        - 纪霆舟 -> 纪念：从余孽观察对象到身体上先护住的小孩
        - 纪念 -> 沈清棠：从原书设定里的对手，改成必须审慎接近的新妹妹
        - 沈清棠 -> 纪念：从观察到理解到结盟

        ## 造型状态

        - 话 1：脏卷发、旧衣服、脸脏、营养不良
        - 话 4 后：换新衣，但旧伤还在
        - 沈清棠入府时：整洁、有秩序、视觉上与纪念形成对照

        ## 道具链

        - 点心 -> 最早羞辱与试探
        - 药纸 -> 后续药线核心
        - 旧照片 -> 旧案和终局回收
        """,
    )

    write_text(
        OUT / "样章长稿/第001话.md",
        """
        # 第001话 狗洞

        - 对应原著：开篇-第2章
        - 本话奖励：认下纪念这张脸和她的野劲
        - 本话结尾：点心落湖，父女危险关系成立

        ## Scene 1 | 大堂失控
        - 空间：研究汇报现场 -> 突然切进纪家旧院
        - 目标：让读者在 3 页内完成“穿越 + 被追打 + 危险家宅”的认知
        - 动作：纪念从成年研究生一句荒诞开场，被骂声和鞭子硬拽进新身体
        - 关键视觉：成年人语言塞进五岁女孩身体里，形成第一重荒诞

        ## Scene 2 | 楼梯和狗洞
        - 空间：破楼梯、瘸腿椅子、草丛边狗洞
        - 目标：把求生本能做成动作戏
        - 冲突：肥婆逼近，系统插话，但纪念根本不完全信系统
        - 动作：跑、回头、骂、挠屁股、咬牙钻洞
        - 关键视觉：成人只能塞屁股的小洞，孩子正好能钻出去

        ## Scene 3 | 草丛、树和系统说明
        - 空间：庄园边缘、树下
        - 目标：最短时间把“她不是团宠，是炮灰亲女儿”交待清楚
        - 动作：纪念边喘边接系统设定，嘴上还在跑火车
        - 关键视觉：身体快饿死，脑子还在吐槽原书

        ## Scene 4 | 湖心亭的男人
        - 空间：湖边亭中，桌上摆满点心
        - 目标：让纪霆舟第一次出场就带着非正常人的压迫感
        - 动作：纪念看人看点心，两件事同时发生；纪霆舟抬眼，血色一闪而过
        - 关键视觉：逆光里的男人像神像也像恶鬼

        ## Scene 5 | 夸他好看
        - 目标：用一句不知羞的夸奖把气氛拧歪
        - 动作：纪念仰头夸，纪霆舟反问
        - 场尾推动：纪念说出“好看到我爸见了都要下奶”
        """,
    )

    write_text(
        OUT / "样章长稿/第002话.md",
        """
        # 第002话 点心落湖

        - 对应原著：第2章-第4章
        - 本话奖励：纪霆舟的危险和纪念的厚脸皮同时成立
        - 本话结尾：纪霆舟把她带进自己的生活范围

        ## Scene 1 | 求吃的
        - 纪念盯的是点心，也在盯这个男人会不会心软
        - 她低头求食，嘴巴却还是欠

        ## Scene 2 | 点心落湖
        - 纪霆舟故意拿起点心，在她以为有戏时扔进湖里
        - 这是他第一次把她当小动物逗，也是第一次真正测试她

        ## Scene 3 | 系统揭底
        - 系统提醒这就是渣爹
        - 纪念短暂想走，但发现自己离不开生存资源

        ## Scene 4 | 危险观察
        - 纪霆舟近距离观察她，想知道这孩子身后到底是谁
        - 纪念也在观察：这人漂亮，但心坏

        ## Scene 5 | 被带走
        - 两个人都没明说，但都做出选择
        - 纪霆舟转身，等她自己跟上
        - 纪念知道自己这次不是捡到哥哥，是摸进了龙潭
        """,
    )

    write_text(
        OUT / "样章长稿/第003话.md",
        """
        # 第003话 发烧夜

        - 对应原著：第11章-第13章
        - 本话奖励：父女身体距离突然拉近，关系开始失控
        - 本话结尾：纪霆舟第一次记住“纪念”这个名字

        ## Scene 1 | 夜里发烧
        - 纪念烧得糊涂，求生本能却精准地抓住了最不该抓的人

        ## Scene 2 | 纪霆舟想丢又没丢
        - 他嫌麻烦、嫌脏、嫌自己为什么记得医生说过的话
        - 但动作上还是先照做了

        ## Scene 3 | 孩子梦呓
        - 纪念烧糊涂时的依赖是无意识的
        - 正因为无意识，才更击中纪霆舟

        ## Scene 4 | 一句名字
        - 他终于把“那个小蠢货”替换成“纪念”
        - 这不是嘴上的改变，是心里开始给她留位置
        """,
    )

    write_text(
        OUT / "分页脚本/第001话.md",
        """
        # 第001话 分页脚本

        - 目标页数：20
        - 路由：`paged-comic`
        - 页面总目标：把“逃命 -> 设定翻面 -> 湖心亭见父”做成高抓力开篇

        ## P01
        - 功能：荒诞开场
        - 焦点：成年口吻出现在小女孩身上

        ## P02
        - 功能：鞭子和追打
        - 焦点：危险逼近

        ## P03
        - 功能：孩子视角的楼梯压迫
        - 焦点：成人腿、鞭子、楼梯

        ## P04
        - 功能：系统第一次出声
        - 焦点：纪念停住的脸

        ## P05
        - 功能：翻页点 1
        - 焦点：狗洞位置暴露

        ## P06-P07
        - 功能：钻洞与草丛脱逃
        - 焦点：动作连续感

        ## P08-P09
        - 功能：系统解释炮灰设定
        - 焦点：纪念边喘边吐槽

        ## P10
        - 功能：页尾亮点
        - 焦点：树缝里闪出的湖光

        ## P11-P12
        - 功能：翻页点 2
        - 焦点：湖心亭里坐着的人

        ## P13-P15
        - 功能：纪霆舟危险出场
        - 焦点：逆光、血丝、点心盘

        ## P16-P17
        - 功能：纪念被脸吸过去
        - 焦点：孩子仰头，男人垂眼

        ## P18
        - 功能：翻页点 3
        - 焦点：哥哥你真好看

        ## P19-P20
        - 功能：话尾金句
        - 焦点：好看到我爸见了都要下奶
        """,
    )

    write_text(
        OUT / "分页脚本/第002话.md",
        """
        # 第002话 分页脚本

        - 目标页数：20
        - 页面总目标：把纪霆舟的危险试探和纪念的厚脸皮锁住

        ## P01-P03
        - 纪念求吃的
        - 点心、口水、抬眼

        ## P04
        - 翻页点：系统提醒“这是你爹”

        ## P05-P07
        - 纪霆舟把点心扔进湖里
        - 重点是羞辱感和危险美感同时成立

        ## P08-P10
        - 纪念短暂想撤，但撤不起

        ## P11-P14
        - 纪霆舟细看这个孩子
        - 这里用近景，不用太多解释

        ## P15-P17
        - 她决定跟上
        - 他决定让她跟

        ## P18-P20
        - 话尾：生活空间被打开，但不是庇护，是更深的未知
        """,
    )

    panel_script = []
    panel_rows = [
        (1, 1, "纪念成年口吻开场，下一秒切到五岁身体", "纪念", "汇报台与旧院声音重叠", "“你好，我叫纪念——”", "标题页兼人设炸点"),
        (1, 2, "鞭子呼啸，直接打断开场", "肥婆", "鞭子甩进画面", "", "用动作切穿文字"),
        (2, 1, "孩子视角看见冲来的成年人", "肥婆的腿和鞭子", "纪念回头", "", "压迫感"),
        (2, 2, "纪念吐槽不是玩Sm的", "纪念", "边跑边想", "“那肯定不是玩Sm的。”", "黑色幽默"),
        (3, 1, "系统第一次出声", "纪念的耳边空白", "她一愣", "【右面。】", "气泡用异形框"),
        (3, 2, "瘸腿椅子和狗洞同时入画", "椅子后的洞", "纪念急转", "", "信息揭示"),
        (4, 1, "纪念钻洞，身体几乎贴地", "孩子身体", "爬、蹭、钻", "", "动作格"),
        (4, 2, "洞外草丛和洞内肥婆形成对比", "狗洞出口", "纪念滚出去", "", "节奏松开"),
        (5, 1, "肥婆没抓住她", "洞口被堵住的脸", "肥婆趴洞口骂", "", "翻页前压一下"),
        (5, 2, "纪念瘫在树下喘", "纪念的胸口", "大喘气", "“这到底怎么回事。”", "翻页后解释段前留白"),
        (6, 1, "系统讲原书设定", "纪念和空白气泡", "她靠树听", "【你穿书了。】", "设定要短"),
        (6, 2, "纪念吐槽书名", "纪念翻白眼", "她抠头发", "“这文名一听就清水。”", "继续锁口气"),
        (7, 1, "她快饿昏，看到湖光", "树缝光点", "她眯眼", "", "转场"),
        (7, 2, "湖心亭远景", "亭中一人一桌", "纪念小小站在前景", "", "建立场面"),
        (8, 1, "纪霆舟抬眼", "眼睛和逆光脸", "微抬下巴", "", "首次正脸"),
        (8, 2, "纪念看人也看点心", "点心盘", "吞口水", "", "双焦点但以点心为主"),
        (9, 1, "她夸他好看", "纪念", "仰头", "“哥哥，你真好看。”", "角色关系错位"),
        (9, 2, "纪霆舟反问", "纪霆舟", "垂眼", "“哦？有多好看。”", "冷"),
        (10, 1, "纪念站直", "纪念的小胸脯", "她认真组织措辞", "", "笑点前蓄力"),
        (10, 2, "她说出金句", "纪念的嘴", "一本正经", "“好看到我爸见了都要下奶！”", "本话最大钩子"),
    ]
    for page, panel, purpose, focus, action, dialogue, note in panel_rows:
        panel_script.append(
            {
                "page": page,
                "panel": panel,
                "purpose": purpose,
                "focal_point": focus,
                "characters": ["纪念"] if "纪念" in focus or "纪念" in purpose else ["纪霆舟"],
                "action": action,
                "dialogue": dialogue,
                "balloon_note": note,
                "transition": "顺切" if panel > 1 else "翻页/场切",
            }
        )
    write_json(OUT / "分格脚本/第001话.json", panel_script)

    write_text(
        OUT / "对白打磨记录.md",
        """
        # 对白打磨记录

        ## 主要角色口吻地图

        - 纪念：嘴快、野、比喻脏但准，常用错位夸奖和荒诞吐槽
        - 纪霆舟：短、冷、懒得解释，越危险时越少字
        - 沈清棠：克制、整洁、情绪压在句尾
        - 陈默：更少字，像在削句子

        ## 本轮重点改写

        1. 把小说里的长段系统说明压成短句和动作停顿。
        2. 保留纪念的野口气，但控制单格字量，避免一格里讲三层意思。
        3. 纪霆舟的对白原则是“越重要越短”，不让他跟纪念一样会说。

        ## 删除的坏味道

        - 设定型复述
        - 明说“我很害怕/我很饿”
        - 作者替角色解释关系

        ## 保留的强句

        - “哥哥，你真好看。”
        - “好看到我爸见了都要下奶！”
        - “这文名，一听就清水。”
        """,
    )

    write_text(
        OUT / "评估复盘.md",
        """
        # 评估复盘

        ## 结论

        当前样章批可以继续进入下一轮，但不能直接扩完整长稿。

        ## 已成立

        - 开篇抓力强，狗洞和湖心亭成立
        - 纪念口气成立，没有被洗成通用团宠女主
        - 纪霆舟的危险美感成立
        - 第 1 话的页尾钩子够硬

        ## 仍不够

        - 分页脚本还偏“影视感拆页”，页面自己的呼吸不够明确
        - 前 3 话里沈清棠的影子铺得还不够早
        - 支撑型角色的视觉锚点还薄
        - 孩子视角虽然强，但“无声页”还不够，台词偏多

        ## 判断

        - 允许继续进入审计、理论评议、仇人负评和源场景回捞
        - 不允许直接扩到完整 30 话长稿
        """,
    )

    write_text(
        OUT / "技法使用审计.md",
        """
        # 技法使用审计

        ## 本轮确实用到的技法

        - McCloud 的 closure：第 1 话狗洞逃命大量依赖格间补完
        - McCloud 的图标化与遮罩：纪念表情更图标化，庄园和亭子更写实
        - Eisner 的连续艺术原则：把动作、气泡和空间一起组织
        - Framed Ink 的叙事构图：湖心亭出场不追求漂亮，追求“危险的好看”
        - 报告里的“画面优先”：系统说明尽量压短，把饥饿、危险和压迫交给动作

        ## 本轮用得不够好的技法

        - 页面节奏：分页仍偏事件推进，呼吸页还不够
        - 角色资产化：支撑型角色的视觉锚点还不够强

        ## 本轮没采用的 GitHub 思路

        - 没采用“一句 prompt 直接出漫画”的 AI Comic Factory 路径
        - 没采用 StoryDiffusion 的图像先行逻辑，只保留一致性管理思路
        - 没把 Storyboarder 的镜头语言直接当页面语言
        """,
    )

    write_text(
        OUT / "理论依据评议.md",
        """
        # 理论依据评议

        ## 成立的地方

        ### 1. 开篇事件抓力成立
        - 证据：`第001话` 的狗洞逃命和湖心亭见父
        - 理由：第一话没有被设定说明拖死，而是以动作和视觉钩子推进
        - 理论依据：报告强调“文字时间流要转成可被视觉快速解码的连续艺术”

        ### 2. 纪念的视觉-语言双重识别度成立
        - 证据：乱卷发、小身形、狠口气、抓袖子和脏比喻同时保留
        - 理由：角色没有被洗成一般儿童主角
        - 理论依据：McCloud 的图标化抽象要求角色用更强的识别符号进入读者代入区

        ### 3. 纪霆舟出场具有明确构图意图
        - 证据：逆光、长腿、坐姿、点心盘
        - 理由：不是只画帅，而是明确传达“危险、好看、不可亲近”
        - 理论依据：`Framed Ink` 的构图功能原则

        ## 失败的地方

        ### 1. 分页还偏影视拆镜
        - 证据：`分页脚本/第001话.md` 里部分页仍像镜头连拍的拆页说明
        - 理由：页面自己的“停顿”和“翻页压重”还不够明确
        - 理论依据：Eisner 和报告都强调漫画不是电影帧切片

        ### 2. 无声页与静默格不足
        - 证据：第 2 话几乎每个重点都配了文字
        - 理由：孩子观察父亲的页面，本应允许更长的沉默
        - 理论依据：McCloud 的时刻到时刻、视角到视角过渡
        """,
    )

    write_text(
        OUT / "仇人式负评.md",
        """
        # 仇人式负评

        这版最像样的地方是开篇真有劲，但往后已经开始露出“作者太会了，所以谁都不许闭嘴”的毛病。

        我作为一个脾气很差的读者，会这样骂：

        1. 纪念是成立的，纪霆舟也成立，但一到分页脚本就开始有点像“把电影镜头拆到纸上”，不是漫画自己在呼吸。
        2. 你明明知道孩子视角是宝，结果还是忍不住用太多嘴巴说明。
        3. 你嘴上说沈清棠不是工具人，可前 3 话里她的存在感还只是影子，不够早。
        4. 你说这是漫画，不是分镜表，那支撑角色为什么还没有更硬的视觉锚？

        现在的问题不是不会写，是还没彻底放弃影视惯性。
        """,
    )

    write_text(
        OUT / "编辑导演修订建议.md",
        """
        # 编辑导演修订建议

        ## 编辑侧

        1. 前 5 话必须更早铺沈清棠的有效存在，不要等她进门才开始算人物。
        2. 前 10 话的每话奖励要更明确区分：生存、靠近、看见、站位、结盟。
        3. 前 50 章具体改编应该压成前 10 话，不宜再稀释。

        ## 页面叙事侧

        1. 增加无声页和静默大格，让孩子观察大人的危险感真正长出来。
        2. 强化孩子视角的高度差，不要一到解释就回到平视镜头。
        3. 支撑角色必须各有一个视觉锚，不然页面里会糊成“另一个大人”。

        ## 写回 skill 的规则

        1. 当主角是儿童时，前 10 话默认以儿童视线高度组织成人压迫。
        2. 每个进入前 10 话主舞台的支撑角色，必须有一个视觉锚道具或姿态。
        3. 每话至少要设计一个“文字明显减少、只靠画面推进”的静默段。
        """,
    )


if __name__ == "__main__":
    main()

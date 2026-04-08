from pathlib import Path
from html import escape

OUT_DIR = Path('/home/ubuntu/.openclaw/workspace/projects/tigrox-playbook')

EN = {
    'lang': 'en',
    'title': 'Tigrox Tiger Milk King — Ad Bounty Playbook v1.0',
    'hero_kicker': 'Ad Bounty Playbook',
    'hero_title': 'Tigrox Tiger Milk King (TMK)',
    'hero_subtitle': 'A premium direct-response playbook for cough, airway comfort, lung care, and family relief.',
    'positioning': 'Market-leading Tiger Milk Mushroom lung support drink',
    'meta': [
        ['Positioning', 'Market-leading Tiger Milk Mushroom lung support drink'],
        ['Audience', 'Cough, smoker, post-viral, caregiver segments'],
        ['Creative mode', 'Premium empathy + root-cause sales narrative']
    ],
    'overview_title': 'Big Opportunity — Read This First',
    'intro': [
        'Malaysia\'s cough and respiratory wellness market is huge. Families worry when a child keeps coughing at night, smokers fear what years of damage may be doing, and post-viral cough sufferers feel trapped in a symptom that refuses to end.',
        'That is the opening for Wellous Tigrox Tiger Milk King. The product is positioned as a premium, natural, easy-to-drink lung support liquid that feels more practical than bitter traditional brews and more meaningful than cheap red syrups that only numb symptoms for a while.',
        'The sales story is not just “stop coughing.” It is about helping people breathe more freely, sleep without fear, protect family members, and feel they are finally addressing the root of the problem.'
    ],
    'stats': [
        ['Daily use', '20ml once a day'],
        ['Format', 'Liquid botanical nutritional drink'],
        ['Taste', 'Sweet-sour citrus profile'],
        ['Offer frame', 'Family bundle + risk-free refund assurance']
    ],
    'sections': [
        {
            'id': 'product', 'icon': '🏆', 'title': 'Hero Product Snapshot',
            'blocks': [
                {'type': 'feature', 'eyebrow': 'Hero Product', 'title': 'What TMK is', 'text': 'Wellous Tigrox Tiger Milk King is a once-daily 20ml botanical lung wellness drink built around Tiger Milk Mushroom (Lignosus rhinocerus), licorice, and citrus. It is presented as a premium, fast-to-take liquid that avoids the pain points of bitter herbal decoctions and hard-to-swallow pills.'},
                {'type': 'grid', 'items': [
                    ['Pleasant taste', 'Designed to feel like a fruity liquid rather than “medicine punishment,” which matters for children and older adults.'],
                    ['Root-cause frame', 'Positioned as helping clear the lungs and soothe inflamed airways instead of merely suppressing the cough reflex.'],
                    ['Family-safe perception', 'No sleepy syrup identity, no “heavy chemical” impression, and suitable for broad household use in messaging.'],
                    ['Premium-value logic', 'Expensive upfront, but framed as cheaper than repeated clinic visits, missed work, wasted remedies, and family stress.']
                ]}
            ]
        },
        {
            'id': 'brand', 'icon': '💎', 'title': 'Brand Perception & Emotional Territory',
            'blocks': [
                {'type': 'text', 'text': 'The brand should feel premium, credible, calm, and deeply empathetic. The voice is not a loud miracle-seller. It should sound like a warm, high-trust respiratory expert who understands how draining chronic coughing can be.'},
                {'type': 'quote', 'items': [
                    'Move the audience from fear, embarrassment, and sleeplessness → to clear breathing, calm mornings, and family peace.',
                    'Make them feel past failures were not their fault; they were simply using solutions that never addressed the real issue.',
                    'Treat Tiger Milk Mushroom as a prized Malaysian ingredient with heritage, seriousness, and modern value.'
                ]},
                {'type': 'list', 'title': 'What everyone should know about the brand', 'items': [
                    'Uses a prized Tiger Milk Mushroom story: cultivated for 270 days and slowly simmered at 65°C to signal care and potency.',
                    'Sold as a genuine root-support product, not a drowsy sugar syrup.',
                    'Special advantage: easy enough to give without daily battles at home.'
                ]}
            ]
        },
        {
            'id': 'mechanism', 'icon': '🔬', 'title': 'Main Ingredient Mechanism of Action',
            'blocks': [
                {'type': 'cards', 'items': [
                    ['Targeted clearing', 'Tiger Milk Mushroom is framed as reaching the airways, easing inflammation, and helping loosen stubborn phlegm and long-term residue in the lungs.'],
                    ['Soothing and repair', 'Licorice is positioned as the fast comfort layer: soothing the throat, reducing irritation, and helping the mucosal lining recover after persistent coughing.'],
                    ['Long-term resilience', 'Daily 20ml use is framed as strengthening respiratory defense over time, building a “protective coat” for the lungs against future irritation.']
                ]}
            ]
        },
        {
            'id': 'audience', 'icon': '🎯', 'title': 'Target Audience Personas',
            'blocks': [
                {'type': 'persona', 'items': [
                    ['🚬', 'The Stubborn Smoker', 'Morning black phlegm, hidden fear of long-term damage, and refusal to openly admit vulnerability.'],
                    ['🤱', 'The Exhausted Mother', 'Sleepless nights, recurring child cough episodes, guilt over forcing bitter medicine, and fear of escalation.'],
                    ['💼', 'The Post-Viral Office Worker', 'Months of lingering dry cough, embarrassment in meetings, fear of being judged as contagious, and lost confidence.'],
                    ['👵', 'The Dutiful Adult Child', 'Worry about coughing parents at night, readiness to spend for the best solution, and frustration when elders reject bitter remedies.']
                ]},
                {'type': 'text', 'text': 'Core audience range: Malaysian adults aged roughly 25–65 with enough spending power to choose a premium solution when fear, guilt, frustration, or repeated failure makes the problem feel urgent.'}
            ]
        },
        {
            'id': 'desires', 'icon': '🫁', 'title': 'Core Desires to Sell Into',
            'blocks': [
                {'type': 'desire', 'items': [
                    ['Sleep through the night without fear', 'Sell relief from anxious midnight listening and chronic sleep disruption.'],
                    ['Breathe deeply without triggering a coughing fit', 'Restore dignity at work, in public, and during daily movement.'],
                    ['Stop fighting with family over medicine', 'Taste and convenience become emotional conversion tools, not secondary features.'],
                    ['Feel like I am protecting them, not failing them', 'Premium ingredients help caregivers feel they are finally giving loved ones the best.'],
                    ['Repair the damage quietly', 'For smokers, make it about private restoration, not public scolding or forced quitting.']
                ]}
            ]
        },
        {
            'id': 'triggers', 'icon': '⚡', 'title': 'Trigger Events That Create Buyers',
            'blocks': [
                {'type': 'timeline', 'items': [
                    ['2 AM barking cough', 'A parent hears a frightening hollow cough and wants something stronger than ordinary syrup immediately.'],
                    ['The elevator stare', 'A dry cough erupts in a quiet lift or meeting room and creates social shame.'],
                    ['Black phlegm in the sink', 'A smoker sees dark sputum in the morning and feels a sudden wave of health fear.'],
                    ['Rejected bitter medicine', 'Hours spent preparing herbal remedies end in refusal, waste, and frustration.'],
                    ['The cold that never ends', 'Weeks or months after recovery, the throat still feels raw and the cough still lingers.']
                ]}
            ]
        },
        {
            'id': 'creative', 'icon': '🔥', 'title': 'Winning Creative Directions',
            'blocks': [
                {'type': 'columns', 'left_title': 'Current winning formats', 'left_items': [
                    'Short pain-point videos built around frightening cough sounds.',
                    'Educational explainer content: why sweet syrups only “trick” the throat.',
                    'Long-form testimonials, family stories, and doctor-style soft-sell VSLs.'
                ], 'right_title': 'Angles the brand wants', 'right_items': [
                    'Mechanism angle — explain why 20ml liquid absorption matters.',
                    'Symptom angle — black phlegm, midnight cough, lingering post-viral irritation.',
                    'Identity restoration angle — restore dignity, confidence, and breathing ease.',
                    'Root-cause angle — contrast TMK with symptom-masking red syrups.'
                ]},
                {'type': 'list', 'title': 'High-converting hook directions', 'items': [
                    'The Sound of Fear — start with a cough that instantly activates caregiver anxiety.',
                    'The Toilet Sink Confession — speak directly to smokers who see black phlegm every morning.',
                    'The Deceptive Red Syrup — challenge the “just take syrup” assumption.',
                    'The Failed TCM Hook — “Three hours of boiling, one second to spit it out.”',
                    'The 100-Day Post-Covid Hook — lingering dry cough long after the virus is gone.',
                    'The Guilty Daughter Hook — hearing a parent cough through the wall at night.',
                    'The Tear-Open Liquid Hook — convenience, portability, and immediate usability.'
                ]}
            ]
        },
        {
            'id': 'claims', 'icon': '⚖️', 'title': 'Claims Rules & Compliance Guardrails',
            'blocks': [
                {'type': 'do_dont', 'do_title': 'You can say', 'do_items': [
                    'Helps soothe the throat and ease cough discomfort.',
                    'Traditionally used to support lung and respiratory wellness.',
                    'Easy-to-drink liquid with a taste children may accept more readily.',
                    'Contains natural botanicals such as Tiger Milk Mushroom, licorice, and citrus.',
                    'A daily support option for smokers and people bothered by recurrent cough.'
                ], 'dont_title': 'You cannot say', 'dont_items': [
                    'Do not claim to 100% cure asthma, pneumonia, or severe diseases.',
                    'Do not use miracle language like “magic cure” or “medical miracle.”',
                    'Do not say this replaces prescribed medicine.',
                    'Do not imply people can keep smoking without consequences because of the product.'
                ]},
                {'type': 'warning', 'text': 'Avoid disgusting imagery, gore, and cheap miracle-seller energy. The brand must stay premium and medically sensible.'},
                {'type': 'list', 'title': 'Words to avoid completely', 'items': [
                    'Miracle cure', 'Cures everything', 'Lung cancer killer', '100% eradication', 'Instant one-second effect', 'Medical miracle', 'Cheap', 'Budget substitute'
                ]}
            ]
        },
        {
            'id': 'competitors', 'icon': '⚔️', 'title': 'Competitor Framing',
            'blocks': [
                {'type': 'cards', 'items': [
                    ['Traditional herbal brews', 'Too troublesome, too bitter, too slow, and often rejected by the person who actually needs to drink them.'],
                    ['Cheap over-the-counter syrups', 'Symptom masking, sleepy-child associations, chemical perception, and rebound frustration when the cough returns.'],
                    ['Hospital visits & nebulizer routines', 'Expensive, stressful, time-consuming, and emotionally hard on both children and caregivers.']
                ]}
            ]
        },
        {
            'id': 'objections', 'icon': '🧠', 'title': 'Objection Handling & Real Customer Language',
            'blocks': [
                {'type': 'qa', 'items': [
                    ['“This is a scam.”', 'Acknowledge the skepticism. The market is full of sugary, low-substance products, so the creative must emphasize credible ingredients, real user proof, and substance over celebrity hype.'],
                    ['“It\'s too expensive.”', 'Reframe against ER visits, missed work, wasted remedies, sleepless nights, and repeated family stress.'],
                    ['“It must taste bad.”', 'Taste is a major conversion advantage — a sweet-sour citrus liquid that removes the daily resistance battle.'],
                    ['“I\'ve been coughing for years. Nothing works.”', 'Frame the issue as long-term buildup that requires deeper, more patient support — not another surface-level syrup.' ]
                ]},
                {'type': 'list', 'title': 'Use the customer\'s own language', 'items': [
                    '“It feels like sandpaper in my throat.”',
                    '“That barking dry cough in the middle of the night.”',
                    '“Every morning I feel like I\'m coughing my lungs out over the sink.”',
                    '“That wet rattling cough keeps me awake all night.”',
                    '“Every medicine time feels like a war.”'
                ]}
            ]
        },
        {
            'id': 'matrix', 'icon': '🏛️', 'title': 'Positioning Matrix, Do/Don’t, and Sellable Numbers',
            'blocks': [
                {'type': 'grid', 'items': [
                    ['Mechanism', 'A highly absorbable 20ml liquid that quickly reaches the throat and lungs.'],
                    ['Root cause', 'Use natural ingredients to support clearing, soothing, and restoration instead of numbing symptoms.'],
                    ['Ingredients', 'Tiger Milk Mushroom + licorice + citrus = premium lung support with comfort and taste.'],
                    ['Value', 'A small daily spend positioned as better sleep, less panic, and less wasteful medical spending.']
                ]},
                {'type': 'do_dont', 'do_title': 'Messaging do', 'do_items': [
                    'Show deep empathy for caregiving exhaustion and social embarrassment.',
                    'Emphasize “no boiling” and “pleasant taste.”',
                    'Use vivid but not disgusting scenes: midnight coughing, meeting-room shame, morning phlegm fear.',
                    'Present the product as a premium protective shield for the family.',
                    'Do the math for the customer: sleep, time, clinic visits, and emotional cost.'
                ], 'dont_title': 'Messaging don’t', 'dont_items': [
                    'Do not overclaim disease cures.',
                    'Do not make the brand look like a cheap supermarket syrup.',
                    'Do not shame smokers like a lecturer.',
                    'Do not hide behind overly technical medical language.',
                    'Do not rely on “stop cough” alone — explain clearing, soothing, and support.'
                ]},
                {'type': 'list', 'title': 'Magic numbers from the source document', 'items': [
                    'Helped over 1,900,000 users improve their breathing wellness story.',
                    '55% of users reportedly upgrade to TMK + Imuglo after feeling a real 30-day change.',
                    'Tiger Milk Mushroom carries 400+ years of indigenous use history.',
                    'Modern science framing: respiratory inflammation response reduction up to 70%.',
                    'Licorice framing: throat comfort and cough-frequency reduction above 40%.'
                ]}
            ]
        }
    ]
}

CN = {
    'lang': 'zh-CN',
    'title': 'Tigrox 虎乳芝王 — 广告赏金简报 v1.0',
    'hero_kicker': '广告赏金简报',
    'hero_title': 'Tigrox 虎乳芝王 (TMK)',
    'hero_subtitle': '基于最新版文档重建的高级单页广告打法站点，聚焦咳嗽、呼吸道保养、补肺与家庭安心。',
    'positioning': '市场第一虎乳芝补肺饮',
    'meta': [
        ['品牌定位', '市场第一虎乳芝补肺饮'],
        ['核心人群', '久咳、烟民、病后久咳、照顾者人群'],
        ['创意打法', '高级共情 + 治本型销售叙事']
    ],
    'overview_title': '🚀 Big Opportunity — 先看这一段',
    'intro': [
        '马来西亚的咳嗽健康市场非常大。孩子半夜一直咳、老人反复咳、抽烟多年的人早上咳黑痰、感冒后久咳不愈——这些都不是小痛点，而是会持续消耗一个家庭的睡眠、情绪与安全感。',
        'Wellous Tigrox Tiger Milk King 的机会，就在于它不是传统苦中药，也不是只会暂时压住症状的廉价红色糖浆。它被包装成一个高级、天然、好喝、方便、真正补肺保养的液体方案。',
        '这套销售逻辑不能只停留在“止咳”。真正要卖的是：更顺的呼吸、更安稳的睡眠、对家人的保护感，以及“终于找到比较治本的方法”的希望。'
    ],
    'stats': [
        ['每日用量', '每天一次，每次 20ml'],
        ['产品形态', '植物营养液 / 液体补肺饮'],
        ['口味印象', '酸甜果汁感，更容易接受'],
        ['销售包装', '家庭套装优惠 + 零风险退款保证']
    ],
    'sections': [
        {
            'id': 'product', 'icon': '🏆', 'title': 'Hero Product — 产品核心',
            'blocks': [
                {'type': 'feature', 'eyebrow': 'Hero Product', 'title': 'TMK 是什么', 'text': 'Wellous Tigrox Tiger Milk King 是一款每天喝一次、每次 20ml 的植物营养液，核心成分包括虎乳芝（Lignosus rhinocerus）、甘草和桔子。它强调高级、方便、易吸收、好入口，解决传统苦中药太难喝、太麻烦，以及大药丸难吞的问题。'},
                {'type': 'grid', 'items': [
                    ['超好喝，不抗拒', '酸甜果汁型液体，比苦中药和大药丸更容易让孩子与老人接受。'],
                    ['主打“治本”逻辑', '不是麻木神经、暂时压咳，而是强调清肺、化痰、舒缓发炎。'],
                    ['全家可放心的感觉', '没有“化学止咳糖浆”的廉价印象，更像长期保养型高级方案。'],
                    ['高价但讲得通', '价格不低，但可以对比急诊、请假、浪费药材与家庭争吵的隐性成本。']
                ]}
            ]
        },
        {
            'id': 'brand', 'icon': '💎', 'title': '品牌感受与情绪定位',
            'blocks': [
                {'type': 'text', 'text': '这个品牌必须给人“高级、有科学道理、温和可信、真的懂客户心累”的感觉。它不是夸张卖神药的地摊感，而是像一位很会安抚人的专业呼吸道顾问。'},
                {'type': 'quote', 'items': [
                    '让用户从“害怕、失眠、尴尬、自责”切换到“呼吸顺了、夜里安静了、家庭轻松了”。',
                    '要告诉客户：以前治不好，不是你没努力，而是你一直在用不对的方法。',
                    '虎乳芝要被塑造成马来西亚国宝级成分，带有传承感、可信度和高级感。'
                ]},
                {'type': 'list', 'title': '品牌必须让大家记住的点', 'items': [
                    '国宝级虎乳芝，种植 270 天，以 65°C 慢熬，每一滴都有高级感与“真材实料”的信号。',
                    '不是喝了想睡觉的红糖水，而是“真正补肺、舒缓、保养呼吸道”的高级解决方案。',
                    '最大差异点之一：好喝到不需要每天上演“逼吃药大战”。'
                ]}
            ]
        },
        {
            'id': 'mechanism', 'icon': '🔬', 'title': '主要成分机制说明',
            'blocks': [
                {'type': 'cards', 'items': [
                    ['靶向消炎与清理', '虎乳芝被描绘成能深入气管，帮助化开顽固浓痰、减轻发炎，并清理肺部深处长期累积的脏东西。'],
                    ['舒缓与黏膜修复', '甘草负责“马上舒服一点”的层面，帮助舒缓喉咙刺激感、减轻频繁咳嗽造成的疼痛，并辅助黏膜修复。'],
                    ['长期免疫力重塑', '每天 20ml 的长期使用逻辑，是帮助肺部建立更稳的防御感，像给呼吸道加上一层保护。']
                ]}
            ]
        },
        {
            'id': 'audience', 'icon': '🎯', 'title': '目标人群画像',
            'blocks': [
                {'type': 'persona', 'items': [
                    ['🚬', '固执的老烟枪', '早上狂咳黑痰，嘴上不承认，心里却很怕身体真的出问题。'],
                    ['🤱', '心累无助的妈妈', '孩子反复咳嗽、半夜睡不了、逼喝苦药像打仗，满满内疚感。'],
                    ['💼', '久咳不愈的上班族', '感冒或新冠后拖很久，会议室和电梯里咳嗽让人很尴尬。'],
                    ['👵', '焦虑的孝顺儿女', '听着父母半夜咳嗽很难受，愿意花钱买最好的，但父母又常拒绝苦药。']
                ]},
                {'type': 'text', 'text': '核心受众大致为马来西亚 25–65 岁中高收入群体。只要情绪痛点够重、问题拖得够久，他们就愿意为高级解决方案买单。'}
            ]
        },
        {
            'id': 'desires', 'icon': '🫁', 'title': '核心欲望 — 真正要卖的东西',
            'blocks': [
                {'type': 'desire', 'items': [
                    ['我想一整晚安心睡觉，不再担惊受怕', '卖的是夜里的安静与长期睡眠恢复，不只是少咳两声。'],
                    ['我想大口深呼吸，不再一吸气就狂咳', '卖的是体面、自信与“我终于像正常人一样呼吸”的感觉。'],
                    ['我想家里不要再因为吃药而吵架', '口味与便利性在这个品类里不是小优点，而是重要转化武器。'],
                    ['我想感觉自己是在保护家人，而不是没照顾好他们', '高级成分让照顾者有“我终于给了家人最好的”心理满足。'],
                    ['我想悄悄修补抽烟造成的伤害', '对烟民，不要卖说教；要卖低对抗、低羞耻感的恢复机会。']
                ]}
            ]
        },
        {
            'id': 'triggers', 'icon': '⚡', 'title': '触发购买的关键时刻',
            'blocks': [
                {'type': 'timeline', 'items': [
                    ['凌晨两点狗叫一样的咳嗽', '把父母瞬间吓醒，立刻想找比普通糖浆更有力的办法。'],
                    ['电梯或会议室里的尴尬咳嗽', '公开场合失控咳嗽，带来很强烈的羞耻与压力。'],
                    ['洗手台里的黑痰', '烟民看到黑痰会突然觉得：我可能真的拖不得了。'],
                    ['被拒绝的苦药', '花时间熬药，结果孩子或老人根本不喝，钱和情绪一起浪费。'],
                    ['一直好不了的小感冒', '病早就过了，咳嗽却拖几个星期甚至几个月，促使用户寻找“更深层”的方案。']
                ]}
            ]
        },
        {
            'id': 'creative', 'icon': '🔥', 'title': '高转化创意方向',
            'blocks': [
                {'type': 'columns', 'left_title': '当前容易赢的内容格式', 'left_items': [
                    '痛点短视频：尤其是各种可怕咳嗽声。',
                    '科普型短视频：解释为什么甜糖浆只是在“骗”喉咙。',
                    '真实故事、妈妈采访、长篇软文与 VSL。'
                ], 'right_title': '品牌想看到的广告角度', 'right_items': [
                    '吸收原理角度：20ml 液体为什么更容易被身体接受。',
                    '症状角度：黑痰、半夜咳、久咳、喉咙像砂纸。',
                    '找回面子角度：恢复体面、呼吸轻松、自信回来。',
                    '解决病根角度：对比廉价糖浆只是压症状。'
                ]},
                {'type': 'list', 'title': '高转化 Hook 方向', 'items': [
                    '害怕的声音：一开始就用让照顾者揪心的咳嗽声。',
                    '洗手台的秘密：直接打中早上咳黑痰的烟民。',
                    '骗人的红色糖浆：挑战用户旧认知。',
                    '失败的苦中药：熬了三小时，一秒钟就被吐掉。',
                    '100 天久咳：病毒早走了，咳嗽却还在。',
                    '内疚的女儿：半夜隔墙听见父母咳嗽的心碎感。',
                    '撕开就喝：强调方便、爽感、即时可执行性。'
                ]}
            ]
        },
        {
            'id': 'claims', 'icon': '⚖️', 'title': 'Claims 规则与合规边界',
            'blocks': [
                {'type': 'do_dont', 'do_title': '你可以说', 'do_items': [
                    '帮助舒服喉咙、减轻咳嗽带来的不适。',
                    '传统上用于保养肺部与呼吸道。',
                    '液体好入口、味道更容易让孩子接受。',
                    '含有虎乳芝、甘草、桔子等天然植物成分。',
                    '适合作为抽烟人群或反复咳嗽人群的日常保养辅助。'
                ], 'dont_title': '你不能说', 'dont_items': [
                    '不能说 100% 治好哮喘、肺炎或严重疾病。',
                    '不能用“神药”“奇迹”这类夸张词。',
                    '不能说喝了它就不需要医生开的药。',
                    '不能暗示抽烟照抽也没关系。'
                ]},
                {'type': 'warning', 'text': '不要用过于恶心、血腥的图像，也不要做成廉价江湖神药风。品牌必须维持高级、可信、讲道理的感觉。'},
                {'type': 'list', 'title': '绝对避免的词', 'items': [
                    '神药', '包治百病', '肺癌克星', '100% 根除', '一秒见效', '医学奇迹', '廉价', '平替'
                ]}
            ]
        },
        {
            'id': 'competitors', 'icon': '⚔️', 'title': '竞品对比打法',
            'blocks': [
                {'type': 'cards', 'items': [
                    ['传统苦中药', '太麻烦、太苦、太难坚持，真正需要喝的人往往最抗拒。'],
                    ['药店便宜糖浆', '只治标不治本，容易让人产生“压一压又回来”的失望感。'],
                    ['医院 / 雾化 / 频繁看诊', '贵、耗时、情绪成本高，尤其对孩子和照顾者压力很大。']
                ]}
            ]
        },
        {
            'id': 'objections', 'icon': '🧠', 'title': '异议处理与真实用户语言',
            'blocks': [
                {'type': 'qa', 'items': [
                    ['“这一定是骗局吧”', '先接受怀疑，再强调虎乳芝的可信度、真实用户反馈，以及“不是靠明星乱吹”的理性形象。'],
                    ['“太贵了”', '把用户拉回长期成本：急诊、请假、浪费药材、半夜失眠、家庭压力。'],
                    ['“肯定很难喝”', '口味是强卖点：酸甜果汁型液体，让服用不再像受刑。'],
                    ['“我咳很多年了，肯定没用”', '把问题重新定义成长期累积，需要更深层、更持续的保养，不是再换一瓶普通糖浆。']
                ]},
                {'type': 'list', 'title': '真实客户会这样说', 'items': [
                    '“就像喉咙里卡着砂纸一样痛。”',
                    '“半夜那种像狗叫一样的干咳。”',
                    '“早上在洗手间感觉快把肺都咳出来了。”',
                    '“听到那种有痰的呼噜声，我整夜都睡不着。”',
                    '“每次喂药都像打仗一样累。”'
                ]}
            ]
        },
        {
            'id': 'matrix', 'icon': '🏛️', 'title': '定位矩阵、Do / Don’t 与会卖货的数据',
            'blocks': [
                {'type': 'grid', 'items': [
                    ['Mechanism / 吸收原理', '20ml 高吸收液体，快速触达喉咙与肺部的使用场景。'],
                    ['Root Cause / 解决病根', '强调清理、舒缓、保养，而不是单纯压症状。'],
                    ['Ingredients / 成分组合', '虎乳芝 + 甘草 + 桔子 = 高级补肺逻辑 + 口感优势。'],
                    ['Value / 真正价值', '每天一小包，换来睡眠、安心、节省长期折腾成本。']
                ]},
                {'type': 'do_dont', 'do_title': 'Messaging Do', 'do_items': [
                    '高度共情用户半夜照顾病人的心累和无奈。',
                    '反复强调“不用煮”“果汁味好喝”。',
                    '画面可以痛，但不要恶心：半夜咳、会议尴尬、黑痰恐惧就够了。',
                    '把产品塑造成保护家人的高级防护盾。',
                    '帮用户算清楚情绪成本、时间成本、看病成本。'
                ], 'dont_title': 'Messaging Don’t', 'dont_items': [
                    '不要夸大成包治百病。',
                    '不要做成超市廉价糖水感。',
                    '不要用老师口吻羞辱烟民。',
                    '不要塞太多普通人听不懂的医学术语。',
                    '不要只说“止咳”，一定要解释为什么更深层。'
                ]},
                {'type': 'list', 'title': '文档里的关键数字', 'items': [
                    '帮助超过 1,900,000 名用户改善呼吸健康故事。',
                    '55% 用户在体验到 30 天变化后会升级购买 TMK + Imuglo。',
                    '虎乳芝拥有超过 400 年的原住民使用历史。',
                    '现代科学话术：呼吸道发炎反应可降低高达 70%。',
                    '甘草的话术：帮助舒缓喉咙，并将咳嗽频次减少 40% 以上。'
                ]}
            ]
        }
    ]
}

STYLE = '''
:root {
  --bg: #07111f;
  --bg-2: #0c1628;
  --surface: rgba(13, 22, 40, 0.82);
  --surface-2: rgba(18, 31, 55, 0.92);
  --surface-3: rgba(28, 42, 70, 0.95);
  --border: rgba(255,255,255,0.1);
  --border-2: rgba(255,255,255,0.16);
  --text: #f5f7fb;
  --muted: #b8c3d9;
  --soft: #8ea0bf;
  --gold: #f6c453;
  --gold-2: #ff9f43;
  --blue: #58a6ff;
  --green: #59d38c;
  --red: #ff7b7b;
  --shadow: 0 24px 70px rgba(0,0,0,0.32);
  --radius: 24px;
  --radius-sm: 18px;
  --max: 1180px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: Inter, -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif;
  background:
    radial-gradient(circle at top left, rgba(246,196,83,0.14), transparent 30%),
    radial-gradient(circle at top right, rgba(88,166,255,0.16), transparent 26%),
    linear-gradient(180deg, var(--bg), var(--bg-2));
  color: var(--text);
  line-height: 1.65;
}
a { color: inherit; }
.wrap { width: min(var(--max), calc(100% - 32px)); margin: 0 auto; }
.hero {
  padding: 54px 0 26px;
}
.hero-card {
  border: 1px solid var(--border);
  background: linear-gradient(180deg, rgba(19,31,55,.9), rgba(11,19,34,.96));
  backdrop-filter: blur(16px);
  border-radius: 32px;
  padding: 34px;
  box-shadow: var(--shadow);
  position: relative;
  overflow: hidden;
}
.hero-card::after {
  content: '';
  position: absolute;
  inset: auto -80px -80px auto;
  width: 240px;
  height: 240px;
  background: radial-gradient(circle, rgba(246,196,83,.22), transparent 68%);
}
.kicker {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--gold);
  font-weight: 800;
}
.hero h1 {
  font-size: clamp(2.2rem, 5vw, 4.2rem);
  line-height: 1.02;
  margin: 14px 0 10px;
  letter-spacing: -.04em;
}
.hero p.lead {
  max-width: 820px;
  color: var(--muted);
  font-size: 1.08rem;
  margin: 0 0 22px;
}
.badges, .stat-grid, .nav-grid, .grid, .cards, .persona-grid, .desire-grid, .timeline, .dual {
  display: grid;
  gap: 14px;
}
.badges { grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); margin-top: 24px; }
.badge, .stat, .mini-card, .card, .persona, .desire, .time-item, .dual-col, .quote-box, .warning {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  backdrop-filter: blur(10px);
}
.badge { padding: 16px 18px; }
.badge .label, .stat .label, .mini-card .label { color: var(--soft); font-size: 12px; text-transform: uppercase; letter-spacing: .1em; }
.badge .value, .stat .value { margin-top: 6px; font-weight: 700; }
.stat-grid { grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); margin: 26px 0 0; }
.stat { padding: 16px 18px; }
.nav-shell { position: sticky; top: 0; z-index: 20; padding: 14px 0; backdrop-filter: blur(10px); }
.nav-grid {
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  background: rgba(8,15,28,.72);
  border: 1px solid var(--border);
  border-radius: 22px;
  padding: 12px;
}
.nav-grid a {
  text-decoration: none;
  padding: 12px 14px;
  border-radius: 14px;
  color: var(--muted);
  transition: .18s ease;
  border: 1px solid transparent;
  font-size: .95rem;
}
.nav-grid a:hover { color: var(--text); border-color: var(--border); background: rgba(255,255,255,.04); }
main { padding: 20px 0 70px; }
.section {
  margin: 22px 0;
  border: 1px solid var(--border);
  border-radius: 28px;
  overflow: hidden;
  background: linear-gradient(180deg, rgba(11,18,32,.92), rgba(9,15,26,.96));
  box-shadow: var(--shadow);
}
.section-head {
  display: flex; align-items: center; gap: 14px;
  padding: 26px 28px 14px;
}
.icon {
  width: 46px; height: 46px; border-radius: 16px;
  display: grid; place-items: center;
  background: linear-gradient(135deg, rgba(246,196,83,.18), rgba(88,166,255,.18));
  border: 1px solid var(--border-2);
  font-size: 22px;
}
.section h2 { margin: 0; font-size: clamp(1.35rem, 2vw, 1.8rem); letter-spacing: -.03em; }
.section-body { padding: 0 28px 28px; }
.section-body > p { color: var(--muted); }
.feature {
  padding: 24px;
  border-radius: 22px;
  background: linear-gradient(135deg, rgba(246,196,83,.12), rgba(88,166,255,.09));
  border: 1px solid var(--border-2);
  margin-bottom: 16px;
}
.feature .eyebrow { color: var(--gold); text-transform: uppercase; font-size: 12px; letter-spacing: .1em; font-weight: 800; }
.feature h3 { margin: 8px 0 10px; font-size: 1.5rem; }
.feature p { margin: 0; color: var(--muted); }
.grid { grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); }
.mini-card { padding: 18px; }
.mini-card strong { display: block; margin: 8px 0 6px; font-size: 1rem; }
.mini-card p { margin: 0; color: var(--muted); font-size: .96rem; }
.cards, .persona-grid, .desire-grid { grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }
.card, .persona, .desire, .time-item, .dual-col { padding: 18px 18px 16px; }
.card h4, .persona h4, .desire h4, .dual-col h4 { margin: 0 0 8px; font-size: 1.03rem; }
.card p, .persona p, .desire p, .dual-col li, .time-item p { margin: 0; color: var(--muted); }
.persona .top { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
.persona .emoji { font-size: 1.45rem; }
.quote-box { padding: 16px 18px; margin: 16px 0; }
.quote-box ul, .list ul, .dual-col ul { margin: 0; padding-left: 18px; }
.quote-box li, .list li, .dual-col li { margin: 8px 0; color: var(--muted); }
.list h3, .subhead { margin: 18px 0 8px; font-size: .85rem; letter-spacing: .12em; text-transform: uppercase; color: var(--soft); }
.timeline { grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }
.time-item h4 { margin: 0 0 8px; }
.dual { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
.warning {
  padding: 16px 18px;
  border-color: rgba(255,123,123,.28);
  background: rgba(125,30,45,.18);
  color: #ffd7d7;
  margin: 16px 0;
}
.warning strong { color: #fff; }
.footer {
  color: var(--soft);
  text-align: center;
  padding: 6px 0 46px;
  font-size: .92rem;
}
@media (max-width: 700px) {
  .hero-card, .section-head, .section-body { padding-left: 18px; padding-right: 18px; }
  .hero-card { padding-top: 26px; }
  .nav-grid { grid-template-columns: 1fr 1fr; }
}
'''

def render_block(block):
    t = block['type']
    if t == 'text':
        return f"<p>{escape(block['text'])}</p>"
    if t == 'feature':
        return f"<div class='feature'><div class='eyebrow'>{escape(block['eyebrow'])}</div><h3>{escape(block['title'])}</h3><p>{escape(block['text'])}</p></div>"
    if t == 'grid':
        items = ''.join(f"<div class='mini-card'><div class='label'>Key point</div><strong>{escape(a)}</strong><p>{escape(b)}</p></div>" for a,b in block['items'])
        return f"<div class='grid'>{items}</div>"
    if t == 'cards':
        items = ''.join(f"<div class='card'><h4>{escape(a)}</h4><p>{escape(b)}</p></div>" for a,b in block['items'])
        return f"<div class='cards'>{items}</div>"
    if t == 'persona':
        items = ''.join(f"<div class='persona'><div class='top'><div class='emoji'>{escape(e)}</div><h4>{escape(a)}</h4></div><p>{escape(b)}</p></div>" for e,a,b in block['items'])
        return f"<div class='persona-grid'>{items}</div>"
    if t == 'desire':
        items = ''.join(f"<div class='desire'><h4>{escape(a)}</h4><p>{escape(b)}</p></div>" for a,b in block['items'])
        return f"<div class='desire-grid'>{items}</div>"
    if t == 'timeline':
        items = ''.join(f"<div class='time-item'><h4>{escape(a)}</h4><p>{escape(b)}</p></div>" for a,b in block['items'])
        return f"<div class='timeline'>{items}</div>"
    if t == 'quote':
        items = ''.join(f"<li>{escape(i)}</li>" for i in block['items'])
        return f"<div class='quote-box'><ul>{items}</ul></div>"
    if t == 'list':
        items = ''.join(f"<li>{escape(i)}</li>" for i in block['items'])
        return f"<div class='list'><h3>{escape(block['title'])}</h3><ul>{items}</ul></div>"
    if t == 'columns':
        left = ''.join(f"<li>{escape(i)}</li>" for i in block['left_items'])
        right = ''.join(f"<li>{escape(i)}</li>" for i in block['right_items'])
        return f"<div class='dual'><div class='dual-col'><h4>{escape(block['left_title'])}</h4><ul>{left}</ul></div><div class='dual-col'><h4>{escape(block['right_title'])}</h4><ul>{right}</ul></div></div>"
    if t == 'do_dont':
        left = ''.join(f"<li>{escape(i)}</li>" for i in block['do_items'])
        right = ''.join(f"<li>{escape(i)}</li>" for i in block['dont_items'])
        return f"<div class='dual'><div class='dual-col'><h4>{escape(block['do_title'])}</h4><ul>{left}</ul></div><div class='dual-col'><h4>{escape(block['dont_title'])}</h4><ul>{right}</ul></div></div>"
    if t == 'warning':
        return f"<div class='warning'><strong>Warning:</strong> {escape(block['text'])}</div>"
    if t == 'qa':
        items = ''.join(f"<div class='card'><h4>{escape(q)}</h4><p>{escape(a)}</p></div>" for q,a in block['items'])
        return f"<div class='cards'>{items}</div>"
    raise ValueError(t)


def render_page(data):
    nav = ''.join(f"<a href='#{s['id']}'>{escape(s['icon'])} {escape(s['title'])}</a>" for s in data['sections'])
    meta = ''.join(f"<div class='badge'><div class='label'>{escape(k)}</div><div class='value'>{escape(v)}</div></div>" for k,v in data['meta'])
    sections = []
    for s in data['sections']:
        blocks = ''.join(render_block(b) for b in s['blocks'])
        sections.append(f"<section class='section' id='{escape(s['id'])}'><div class='section-head'><div class='icon'>{escape(s['icon'])}</div><h2>{escape(s['title'])}</h2></div><div class='section-body'>{blocks}</div></section>")
    stats = ''.join(f"<div class='stat'><div class='label'>{escape(k)}</div><div class='value'>{escape(v)}</div></div>" for k,v in data['stats'])
    intro = ''.join(f"<p>{escape(p)}</p>" for p in data['intro'])
    return f'''<!DOCTYPE html>
<html lang="{data['lang']}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(data['title'])}</title>
  <style>{STYLE}</style>
</head>
<body>
  <div class="wrap hero">
    <div class="hero-card">
      <div class="kicker">🫁 {escape(data['hero_kicker'])}</div>
      <h1>{escape(data['hero_title'])}</h1>
      <p class="lead">{escape(data['hero_subtitle'])}</p>
      <div class="badges">{meta}</div>
      <div class="stat-grid">{stats}</div>
    </div>
  </div>

  <div class="wrap nav-shell">
    <nav class="nav-grid">{nav}</nav>
  </div>

  <main class="wrap">
    <section class="section" id="overview">
      <div class="section-head"><div class="icon">🚀</div><h2>{escape(data['overview_title'])}</h2></div>
      <div class="section-body">{intro}</div>
    </section>
    {''.join(sections)}
  </main>

  <div class="wrap footer">Rebuilt from the latest Tigrox Playbook Version 1.0 source document • Generated by Lisa 🤍</div>
</body>
</html>'''

(OUT_DIR / 'index.html').write_text(render_page(EN), encoding='utf-8')
(OUT_DIR / 'index-cn.html').write_text(render_page(CN), encoding='utf-8')

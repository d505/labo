import os
from django import setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE','login.settings')
setup()

from loginapp.models import TemplateSelect

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "集積回路情報",
    professor = "沼昌宏",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/eng-cas/"

)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "計算機工学",
    professor = "塚本昌彦",
    comment = "",
    url = "https://tt-lab.jp/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "情報通信",
    professor = "森井昌彦",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/eng-es3/"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "アルゴリズム",
    professor = "中村匡秀",
    comment = "",
    url = "https://es4.eedept.kobe-u.ac.jp/"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "知的学習論",
    professor = "小澤誠一",
    comment = "",
    url = "https://kuilt-lab.jp/"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "メゾスコピック材料学",
    professor = "藤井稔",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/eng-nano/"

)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "フォトニック材料学",
    professor = "喜多隆",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/eng-photonics/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "量子機能工学",
    professor = "北村雅季",
    comment = "",
    url = "http://www.ep3-ku.org/index.php"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "ナノ構造エレクトロニクス",
    professor = "小野倫也",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/eng-nanoelectronics/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "電磁エネルギー物理学",
    professor = "竹野裕正",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/eng-em-energy/"
)


TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "システム制御",
    professor = "羅志偉",
    comment = "",
    url = "http://www.research.kobe-u.ac.jp/eng-ro-man/index.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "計算宇宙学科",
    professor = "臼井英之",
    comment = "",
    url = "http://www.lab.kobe-u.ac.jp/csi-usui/"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department ="情報知能工学科",
    image = "",
    room = "システム計測",
    professor = "的場修",
    comment = "",
    url = "http://www.lab.kobe-u.ac.jp/csi-applied-optics/index.html"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department ="情報知能工学科",
    image = "",
    room = "創発計算",
    professor = "玉置久",
    comment = "",
    url = "http://www.csi.kobe-u.ac.jp/organization/laboratory.html"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "システム構造",
    professor = "小林太",
    comment = "",
    url = "http://www.lab.kobe-u.ac.jp/csi-rst/"

)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "メディア情報",
    professor = "滝口哲也",
    comment = "",
    url = "http://www.me.cs.scitec.kobe-u.ac.jp/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "ソフトウェア",
    professor = "藤井信忠",
    comment = "",
    url = "https://kobe-cs18a.github.io/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "情報セキュリティ運用論",
    professor = "鳩野逸生",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "システム知能",
    professor = "熊本悦子",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "システム計画",
    professor = "貝原俊也",
    comment = "",
    url = "http://www21.cs.kobe-u.ac.jp/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "知的データ処理",
    professor = "大川剛直",
    comment = "",
    url = "http://www.cs25.scitec.kobe-u.ac.jp"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "情報システム",
    professor = "永田真",
    comment = "",
    url = "http://www.edu.kobe-u.ac.jp/stin-secafy/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "アーキテクチャ",
    professor = "川口博",
    comment = "",
    url = "https://www28.cs.kobe-u.ac.jp/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "情報通信",
    professor = "太田能",
    comment = "",
    url = "https://www.fine.cs.kobe-u.ac.jp/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "システム数理",
    professor = "佐野英樹",
    comment = "",
    url = "http://www.research.kobe-u.ac.jp/csi-applmath/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "情報数理",
    professor = "桔梗宏孝",
    comment = "",
    url = "http://www.edu.kobe-u.ac.jp/csi-lsi/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "計算分子工学",
    professor = "天能精一郎",
    comment = "",
    url = "http://www.gellan.scitec.kobe-u.ac.jp/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "シミュレーション技法",
    professor = "陰山聡",
    comment = "",
    url = "https://cs52-kobe-u.jp/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "アーキテクチャ",
    professor = "川口博",
    comment = "",
    url = "https://www28.cs.kobe-u.ac.jp/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "計算基盤",
    professor = "横川三津夫",
    comment = "",
    url = "http://www.na.scitec.kobe-u.ac.jp"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "計算流体",
    professor = "坪倉誠",
    comment = "",
    url = "http://www.lab.kobe-u.ac.jp/csi-cfd/index.html"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "計算生物学",
    professor = "田中成典",
    comment = "",
    url = "http://www.na.scitec.kobe-u.ac.jp"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "応用システム(三菱電機)",
    professor = "吉河章二",
    comment = "",
    url = "http://www.na.scitec.kobe-u.ac.jp"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "ソーシャルロボティクス(ATR)",
    professor = "塩見昌裕",
    comment = "",
    url = "http://www.na.scitec.kobe-u.ac.jp"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "知能統合(RIKEN AIP)",
    professor = "上田修功",
    comment = "",
    url = "https://aip.riken.jp"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "応用計算科学(JAMSTEC)",
    professor = "坪井誠司",
    comment = "",
    url = "http://www.na.scitec.kobe-u.ac.jp"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "大規模計算科学(RIKEN R-CCS)",
    professor = "富田浩文",
    comment = "",
    url = "https://www.r-ccs.riken.jp/research/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = "先端流体工学[MH-1]",
    professor = "今井陽介",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/eng-afe/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = "先端流体工学[MH-1]",
    professor = "今井陽介",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = "混相流工学[MH-2]",
    professor = "冨山明男",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/eng-mfd/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = "エネルギー変換工学[MH-3]",
    professor = "浅野 等",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/eng-mh3/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = "先端流体工学[MH-1]",
    professor = "今井陽介",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = "構造安全評価学[MM-1]",
    professor = "阪上隆英",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/eng-solid-mech/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = "破壊制御学[MM-2]",
    professor = "田川雅人",
    comment = "",
    url = "http://www.mech.kobe-u.ac.jp/admission/MM2.pdf"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = "構造機能材料学[MM-3]",
    professor = "田中克志",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/eng-mm4/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = "機能ロボット学[MA-1]",
    professor = "横小路 泰義",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/eng-robotics/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = "センシングデバイス工学[MA-2]",
    professor = "神野伊策",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/eng-dynamics/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = "生産工学[MA-3]",
    professor = "白瀬敬一",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/eng-cimlab/new_index.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = "ナノ機械システム工学[MI-1]",
    professor = "磯野吉正",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/eng-isonolab/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = "材料設計工学[MI-2]",
    professor = "向井敏司",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/eng-mech-mater/index.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "鋼構造研究室",
    professor = "田中剛",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/arch-kussl/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "鋼・コンクリート・合成構造研究室",
    professor = "孫玉平",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/eng-sccs/"
)


TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "建築振動工学研究室",
    professor = "藤谷秀雄",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "安全都市づくり研究室",
    professor = "藤永隆（准教授）",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~ftaka/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "空間創生研究室",
    professor = "山邊友一郎（准教授）",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "建築構造解析研究室",
    professor = "水島靖典（准教授）",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "建築・都市設計研究室",
    professor = "栗山尚子（准教授）",
    comment = "",
    url = "https://audlkobeuniv.wixsite.com/website-kuriyamalab"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "建築意匠・設計研究室",
    professor = "末包伸吾",
    comment = "",
    url = "https://audlkobeuniv.wixsite.com/website-suekanelab"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "建築環境造形研究室",
    professor = "槻橋修",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "建築設計・環境デザイン研究室",
    professor = "光嶋裕介（特命准教授）",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "建築史研究室",
    professor = "中江研",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "生活環境計画研究室",
    professor = "山口秀文（講師）",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/eng-yamaken/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "住環境研究室",
    professor = "近藤民代",
    comment = "",
    url = "http://www.tamiyokondo-lab.jp/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "環境音響学研究室",
    professor = "阪上公博",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/eng-arch-en1/index-j.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "都市環境工学研究室",
    professor = "竹林英樹（准教授）",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~kittaka/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "熱環境解析研究室",
    professor = "高田暁",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/eng-en-hamt/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = "光環境計画研究室",
    professor = "鈴木広隆",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~hisuzuki/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "反応有機化学",
    professor = "森敦紀",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~amori/home/index.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "無機物質創成化学",
    professor = "水畑穣",
    comment = "",
    url = "http://cx2.scitec.kobe-u.ac.jp/index_j.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "膜材料化学",
    professor = "吉岡朋久",
    comment = "",
    url = "http://www.stin.kobe-u.ac.jp/membrane/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "有機合成化学",
    professor = "岡田悦治（准教授）",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~okaetsu/index.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "高分子制御化学",
    professor = "西野孝",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~tnishino/cx4.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "物質物理化学",
    professor = "石田謙司",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/eng-cx1/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "ソフトマター界面機能化学",
    professor = "南秀人",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/eng-cx6/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "機能分析化学",
    professor = "梶並昭彦（准教授）",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~kajinami/index.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "生体機能材料化学",
    professor = "大谷亨（准教授）",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~ooya/index.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "膜工学",
    professor = "松山秀人",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~matuyama/cx14HP/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "触媒反応工学",
    professor = "西山覚",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~ichiy/cx8HP/cx8.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "界面材料工学",
    professor = "丸山達生",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~tmarutcm/index_j.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "移動現象工学",
    professor = "大村直人",
    comment = "",
    url = "https://www.edu.kobe-u.ac.jp/eng-cx9/index.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "粒子流体工学",
    professor = "鈴木洋",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~hidema/fluparlab/"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "バイオ生産工学",
    professor = "近藤昭彦",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~akondo/index.html"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = "生物プロセス工学",
    professor = "山地秀樹",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~katsuda/KindexJ.html"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "食料共生システム",
    image = "",
    room = "水環境学",
    professor = "田中丸治哉",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/ans-water/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "食料環境システム学科",
    image = "",
    room = "土地環境学",
    professor = "澤田豊（准教授）",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/ans-soilenv/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "食料環境システム学科",
    image = "",
    room = "施設環境学",
    professor = "井上一哉",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/ans-hysteng/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "食料環境システム学科",
    image = "",
    room = "地域共生計画学",
    professor = "長野宇規（准教授）",
    comment = "",
    url = "https://rpww.net/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "食料環境システム学科",
    image = "",
    room = "農産食品プロセス工学",
    professor = "井原一高",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/ans-afpel/index.html"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "食料環境システム学科",
    image = "",
    room = "生物生産機械工学",
    professor = "森本英嗣（准教授）",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "食料環境システム学科",
    image = "",
    room = "生物生産情報工学",
    professor = "伊藤博通",
    comment = "",
    url = "https://kobe-u-bioproduction.jp/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "食料環境システム学科",
    image = "",
    room = "圃場機械・栽培学",
    professor = "庄司浩一（准教授）",
    comment = "",
    url = "https://www.edu.kobe-u.ac.jp/ans-foodres/b_03_edu_01.html"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "食料環境システム学科",
    image = "",
    room = "食料経済・政策学",
    professor = "",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "食料環境システム学科",
    image = "",
    room = "農業農村経営学",
    professor = "中塚雅也",
    comment = "",
    url = "https://www.edu.kobe-u.ac.jp/ans-agecon/"
)


TemplateSelect.objects.create(
    faculty = "農学部",
    department = "食料環境システム学科",
    image = "",
    room = "国際食料情報学",
    professor = "石田章",
    comment = "",
    url = "https://www.edu.kobe-u.ac.jp/ans-agecon/"
)


TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "動物遺伝育種学",
    professor = "万年英之",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/gste-animgent/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "動物多様性利用科学",
    professor = "大澤朗",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/ans-koala/main.html"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "生殖生物学",
    professor = "原山洋",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/ans-reprod/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "発生工学",
    professor = "李智博（准教授）",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/ans-reprod/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "栄養代謝学",
    professor = "本田和久",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/ans-nutrition/"
)
TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "動物分子形態学",
    professor = "星信彦",
    comment = "",
    url = "https://nobhoshi.com/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "組織生理学",
    professor = "万谷洋平（助教）",
    comment = "",
    url = "https://nobhoshi.com/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "感染症制御学",
    professor = "佐伯圭一（准教授）",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "動物遺伝資源開発学",
    professor = "大山憲二",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "細胞情報学",
    professor = "中嶋昭雄（准教授）",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/brce-kikkawa/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "資源植物生産学",
    professor = "深山浩",
    comment = "",
    url = "https://kobe-ans-crop.jimdofree.com/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "植物育種学",
    professor = "石井尊生",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/ans-pb/index.html"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "森林資源学",
    professor = "石井弘明",
    comment = "",
    url = "https://forestry-kobe.jimdofree.com/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "園芸植物繁殖学",
    professor = "安田（高崎）剛志",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/ans-hanshoku/index.html"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "園芸生理生化学",
    professor = "",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "熱帯有用植物学",
    professor = "東哲司",
    comment = "",
    url = "https://kobe-ans-tropical.jimdofree.com/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "植物遺伝資源開発学",
    professor = "片山寛則（准教授）",
    comment = "",
    url = "https://www.edu.kobe-u.ac.jp/ans-foodres/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = "食料生産フィールド科学",
    professor = "",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "生物化学",
    professor = "宇野知秀",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/ans-biologicalchemistry/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "食品・栄養化学",
    professor = "橋本堂史（准教授）",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/ans-shokuhin/index.html"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "天然有機分子化学",
    professor = "久世雅樹",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/ans-nprd-chem/index.html"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "有機機能分子化学",
    professor = "",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "植物機能化学",
    professor = "杉本幸裕",
    comment = "",
    url = "https://www.edu.kobe-u.ac.jp/ans-phytochem/lab2022/labtop2022"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "動物資源利用化学",
    professor = "白井康仁",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~shirai/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "植物機能化学",
    professor = "杉本幸裕",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "微生物機能化学",
    professor = "吉田健一",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/ans-applmic/index.html"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "微生物資源化学",
    professor = "竹中慎治",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/ans-hakko3/index.html"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "生物機能開発化学",
    professor = "芦田均",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/ans-frontier/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "土壌学",
    professor = "藤嶽暢英",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/ans-soil/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "植物栄養学",
    professor = "三宅親弘",
    comment = "",
    url = "https://www.p700-oxidation-system.com/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "植物遺伝学",
    professor = "松岡由浩",
    comment = "",
    url = "https://scrapbox.io/KobeUnivPlantGeneticsLab/"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "栽培植物進化学",
    professor = "森直樹",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "細胞機能構造学",
    professor = "中屋敷均",
    comment = "",
    url = "https://www.facebook.com/people/%E7%B4%B0%E8%83%9E%E6%A9%9F%E8%83%BD%E6%A7%8B%E9%80%A0%E5%AD%A6%E7%A0%94%E7%A9%B6%E5%AE%A4-%E7%A5%9E%E6%88%B8%E5%A4%A7%E5%AD%A6%E5%A4%A7%E5%AD%A6%E9%99%A2%E8%BE%B2%E5%AD%A6%E7%A0%94%E7%A9%B6%E7%A7%91/100048870493625/?ref=bookmarks"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "環境物質科学",
    professor = "今石浩正",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/rceg-nowstone/index.html"
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "植物病理学",
    professor = "土佐幸雄",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "昆虫分子機能科学",
    professor = "坂本克彦",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = "昆虫多様性生態学",
    professor = "杉浦真治（准教授）",
    comment = "",
    url = "https://kobe-insect-bioecosys.jimdofree.com/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "分子生理教育研究分野",
    professor = "青沼仁志",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/fsci-aon/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "形質発現教育研究分野",
    professor = "井上邦夫",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/fsci-rna/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "細胞機能教育研究分野",
    professor = "石崎公庸",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/fsci-ishizaki/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "岩崎研究室",
    professor = "岩崎哲史",
    comment = "",
    url = ""
)


TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "大沼研究室",
    professor = "大沼亮",
    comment = "",
    url = "https://onuma-endosymbiosis.com/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "奥田研究室",
    professor = "奥田昇",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "影山研究室",
    professor = "影山裕二（准教授）",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "宮本研究室",
    professor = "宮本昌明",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/fsci-miyalab/index.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "鎌田研究室",
    professor = "鎌田真司",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "川井研究室",
    professor = "川井浩史",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "河村研究室",
    professor = "河村伸一",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "心臓再生研究チーム",
    professor = "木村航",
    comment = "",
    url = "https://www.bdr.riken.jp/ja/research/labs/kimura-w/index.html#members"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "管澤研究室",
    professor = "菅澤薫",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/brce-sugasawa/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "形態進化研究グループ",
    professor = "倉谷滋",
    comment = "",
    url = "http://emo.riken.jp/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "近藤研究室",
    professor = "近藤侑貴（准教授）",
    comment = "",
    url = "https://019.rakusaba.jp/~kondolab/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "形質発現教育研究分野",
    professor = "坂本博",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/fsci-rna/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "生物多様性・進化系統研究室",
    professor = "坂山英俊（准教授）",
    comment = "",
    url = "https://sites.google.com/view/sakayama-lab/home"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "佐倉研究室",
    professor = "佐倉緑（准教授）",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "末次健司研究室",
    professor = "末次健司",
    comment = "",
    url = "https://sites.google.com/site/suetsugujp/home"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "塚本研究室",
    professor = "塚本寿夫",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "辻研究室",
    professor = "辻かおる（准教授）",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "林研究室",
    professor = "林茂生",
    comment = "",
    url = "https://signaling.riken.jp/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "深城研究室",
    professor = "深城英弘",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/fsci-fukaki/fukaki/fukaki_laboratory.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "上井研究室",
    professor = "上井進也",
    comment = "",
    url = ""
)


TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "森田研究室",
    professor = "森田光洋（准教授）",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "呼吸器形成研究チーム",
    professor = "森本充",
    comment = "",
    url = "https://lungdev.riken.jp/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "生物学科",
    image = "",
    room = "大和研究室",
    professor = "大和誠司",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "和田研究室",
    professor = "和田昭英",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~adwada/index.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "笠原研究室",
    professor = "笠原俊二（准教授）",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~kasha/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "大西研究室",
    professor = "大西洋",
    comment = "",
    url = "http://www.edu.kobe-u.ac.jp/sci-onishi/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "枝研究室",
    professor = "枝和男（准教授）",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~eda/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "木村研究室",
    professor = "木村建次郎（学長戦略教授）",
    comment = "",
    url = "https://www.kobe-u.ac.jp/research_at_kobe/NEWS/people/researcher0012.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "小堀研究室",
    professor = "小堀康博",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~ykobori/frame.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "立川研究室",
    professor = "立川貴士",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~tach/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "持田グループ",
    professor = "持田智行",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~mochida/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "固体化学グループ",
    professor = "内野隆司",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~uchino/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "高橋研究室",
    professor = "高橋一志（准教授）",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~kazuyuki/index.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "富永研究室",
    professor = "富永圭介",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~tominaga/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "秋本研究室",
    professor = "秋本誠志（准教授）",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~seiji/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "林研究室",
    professor = "林昌彦",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~mhayashi/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "松原研究室",
    professor = "松原亮介（准教授）",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~ryomatsu/index.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "田村研究室",
    professor = "田村厚夫（准教授）",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/sci-tamura/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "茶谷研究室",
    professor = "茶谷絵理 (准教授)",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~echatani/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "木村哲就研究グループ",
    professor = "木村哲就（准教授）",
    comment = "",
    url = "https://tetsukimura-lab.jp/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "化学科",
    image = "",
    room = "津田研究室",
    professor = "津田明彦（准教授）",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~akihiko/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "物理学科",
    image = "",
    room = "素粒子理論研究室",
    professor = "園田英徳(准教授)",
    comment = "",
    url = "http://octopus.phys.sci.kobe-u.ac.jp/index.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "物理学科",
    image = "",
    room = "宇宙論研究室",
    professor = "早田次郎",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/fsci-pacos/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "物理学科",
    image = "",
    room = "物性理論研究室",
    professor = "久保木一浩（准教授）",
    comment = "",
    url = "http://quattro.phys.sci.kobe-u.ac.jp/Bussei_Riron/index.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "物理学科",
    image = "",
    room = "量子物性論研究室",
    professor = "播磨尚朝",
    comment = "",
    url = "http://www2.kobe-u.ac.jp/~hh/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "物理学科",
    image = "",
    room = "粒子物理学研究室",
    professor = "蔵重久弥",
    comment = "",
    url = "http://ppwww.phys.sci.kobe-u.ac.jp/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "物理学科",
    image = "",
    room = "低温物性物理学",
    professor = "藤秀樹",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/sci-lt/index.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "物理学科",
    image = "",
    room = "極限物性物理学研究室",
    professor = "太田仁",
    comment = "",
    url = "http://extreme.phys.sci.kobe-u.ac.jp/extreme/index_j.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "物理学科",
    image = "",
    room = "電子物性物理学研究室",
    professor = "菅原仁",
    comment = "",
    url = "https://www.lab.kobe-u.ac.jp/sci-denshi/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "惑星科学科",
    image = "",
    room = "地質学教育研究分野",
    professor = "山本由弦",
    comment = "",
    url = "http://www.planet.sci.kobe-u.ac.jp/geol/index_geol.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "惑星科学科",
    image = "",
    room = "岩石学・鉱物学",
    professor = "金子克哉",
    comment = "",
    url = ""
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "惑星科学科",
    image = "",
    room = "固体地球物理学教育研究分野",
    professor = "吉岡祥一",
    comment = "",
    url = "http://www.planet.sci.kobe-u.ac.jp/solidearth/index_solidearth.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "惑星科学科",
    image = "",
    room = "体地球物理学教育研究分野",
    professor = "林祥介",
    comment = "",
    url = "http://epa.scitec.kobe-u.ac.jp/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "惑星科学科",
    image = "",
    room = "惑星宇宙物理学教育研究分野",
    professor = "大槻圭史",
    comment = "",
    url = "http://www.planet.sci.kobe-u.ac.jp/astro/index_astro.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "惑星科学科",
    image = "",
    room = "実験惑星科学教育研究分野",
    professor = "荒川政彦",
    comment = "",
    url = "https://epsl-kobe.sakura.ne.jp/wp/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "惑星科学科",
    image = "",
    room = "観測海洋底科学教育研究分野",
    professor = "島伸和",
    comment = "",
    url = "https://www.research.kobe-u.ac.jp/fsci-marine/"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "惑星科学科",
    image = "",
    room = "計算惑星学教育研究分野",
    professor = "牧野淳一郎",
    comment = "",
    url = "http://www.planet.sci.kobe-u.ac.jp/compute/index_compute.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "惑星科学科",
    image = "",
    room = "惑星地球変動史教育研究分野",
    professor = "宮崎聡教授",
    comment = "",
    url = "http://www.planet.sci.kobe-u.ac.jp/hendou/index_hendou.html"
)

TemplateSelect.objects.create(
    faculty = "理学部",
    department = "惑星科学科",
    image = "",
    room = "応用惑星学教育研究分野",
    professor = "川畑拓矢（客員教授）",
    comment = "",
    url = "http://www.planet.sci.kobe-u.ac.jp/mri/index_MRI.html"
)


#各種初期設定
import random
import shelve #データ保存が可能なモジュール
#プレイヤーのクラス定義
class player:
    def  __init__(self,name,Lv,EXP,NEXTEXP,SP,SS,MAXHP,HP,MAXMP,MP,ATK,DEF,INT):#名前は開始時に追加
        self.name=name
        self.Lv=Lv
        self.EXP=EXP
        self.NEXTEXP=NEXTEXP
        self.SP=SP
        self.SS=SS
        self.MAXHP=MAXHP
        self.HP=HP
        self.MAXMP=MAXMP
        self.MP=MP
        self.ATK=ATK
        self.DEF=DEF
        self.INT=INT
自=player('仮',1,0,10,3,3,20,20,10,10,5,3,5)

class enemy:
    def __init__(self,name,MAXHP,HP,ATK,DEF,EXP):#敵ステータスは[名前,MAXHP,HP,ATK,DEF,EXP]の順
        self.name=name
        self.MAXHP=MAXHP
        self.HP=HP
        self.ATK=ATK
        self.DEF=DEF
        self.EXP=EXP
スライム=enemy('スライム',20,20,7,2,15)
ゴブリン=enemy('ゴブリン',30,30,10,1,30)
グリフォン=enemy('グリフォン',50,50,12,5,50)

class skills:
    def __init__(self,No,name,MP,SP,type,info):
        self.No=No
        self.name=name
        self.MP=MP
        self.SP=SP
        self.type=type
        self.info=info 
S0=skills(0,'火炎切り',6,2,'近接複合攻撃','魔法で剣に炎を宿し切りつけるスキル。ATK、INTの両方に影響を受け、一撃の威力が高い。')
S1=skills(1,'二連切り',6,2,'近接物理攻撃','素早く敵を二回切りつけるスキル。1HITごとのダメージは低くなるため硬い敵には不向き。')
S2=skills(2,'貫通突き',5,2,'近接物理攻撃','剣で鋭く刺し貫くスキル。相手の防御力を無視してダメージを与えることができる。')
S3=skills(3,'ファイアボール',6,2,'遠隔魔法攻撃','魔法で火球を作り打ち出すスキル。魔法の単発高威力担当なので扱いやすい。')
S4=skills(4,'ウィンドバレット',7,2,'遠隔魔法攻撃','魔法で3発の風弾を放つスキル。相手の防御を突破できればゲーム中最高火力。')
S5=skills(5,'サンダーボルト',6,2,'遠隔魔法攻撃','魔法で落雷を呼び寄せるスキル。その雷は敵の防御を無視し大ダメージを与える。')
S6=skills(6,'ヒール',8,3,'回復魔法','魔法で自分のHPを回復するスキル。回復量はINTに依存するので薬草と使い分けよう。')
S7=skills(7,'ATK強化(小)',5,1,'自己強化','3ターンの間自分のATKを少し上げるスキル。通常攻撃にも影響するので侮れない。')
S8=skills(8,'INT強化(小)',5,1,'自己強化','3ターンの間自分のINTを少し上げるスキル。魔法主体で戦うならほぼ必須。')
S9=skills(9,'防御態勢',6,2,'自己強化','3ターンの間防御の構えをとる。効果は通常の防御と同じなので耐久力が驚くほど変わる。')
S10=skills(10,'根性','なし',2,'パッシブ','HPが0になった時にHP1で耐えることができる。ただし一回の戦闘で一回のみ。')
S11=skills(11,'逃げ足','なし',1,'パッシブ','習得していると逃げる時必ず逃げ切れる。いざというときの保険にあると安心。')
S12=skills(12,'最大HP+10','なし',1,'パッシブ','自身の最大HPが10上がる。ステータス底上げ系はLvUPで習得できるので成長を実感できる。')
S13=skills(13,'最大HP+20','なし',2,'パッシブ','自身の最大HPが20上がる。HPが高ければより連戦できるようになるので優先して付けよう。')
S14=skills(14,'最大HP+50','なし',3,'パッシブ','自身の最大HPが50上がる。大きく増えるのでスロットがあれば付けておくべき。')
S15=skills(15,'最大MP+10','なし',1,'パッシブ','自身の最大MPが10上がる。単純にスキルを使える回数が増えるので付け得。')
S16=skills(16,'最大MP+20','なし',2,'パッシブ','自身の最大MPが20上がる。ほぼスキル撃ち放題になるのでこのゲームが目指した爽快感をお試しあれ。')
S17=skills(17,'ATK+2','なし',1,'パッシブ','自身の攻撃力が2上がる。たった2と侮るなかれ、目に見えてダメージが増えるぞ。')
S18=skills(18,'ATK+3','なし',2,'パッシブ','自身の攻撃力が3上がる。圧倒的な攻撃力でぶっ飛ばせ！')
S19=skills(19,'INT+2','なし',1,'パッシブ','自身のINTが2上がる。魔法の効果量に直結するので魔法を使いたいなら必ずセット！')
S20=skills(20,'INT+3','なし',2,'パッシブ','自身のINTが3上がる。魔法がア○ダケダブラみたいな威力になるよ。')
S21=skills(21,'DEF+1','なし',1,'パッシブ','自身の防御力が1上がる。このゲームの防御力はシンプルに減算なので被ダメが1減ります。')
S22=skills(22,'DEF+3','なし',2,'パッシブ','自身の防御力が3上がる。超カチカチでスライムくらいの敵からはほぼ無敵に。')

def スキルセット(a):
    if a.MP=='なし':
        print(a.name,'使用スキルスロット:',a.SP,'分類:',a.type)
    else:
        print(a.name,'消費MP:',a.MP,'使用スキルスロット:',a.SP,'分類:',a.type)
    print(a.info)
    if 自.SP<a.SP:
        print('スキルスロットに充分な空きがありません！')
    else:
        エラー処理=0
        while エラー処理==0:
            try:
                コマンド=-1
                コマンド=int(input('このスキルをセットしますか？(1.はい 2.いいえ):'))
                if コマンド==1 or コマンド==2:
                    エラー処理=1
                else:
                    print('そんなコマンドはありません！')
            except ValueError:
                print('そんなコマンドはありません！')
        if コマンド==1:
            print(自.name,'は',a.name,'をセットした！')
            if a.name=='最大HP+10':
                自.MAXHP=自.MAXHP+10
                自.HP=自.HP+10
            elif a.name=='最大HP+20':
                自.MAXHP=自.MAXHP+20
                自.HP=自.HP+20
            elif a.name=='最大HP+50':
                自.MAXHP=自.MAXHP+50
                自.HP=自.HP+50
            elif a.name=='最大MP+10':
                自.MAXMP=自.MAXMP+10
            elif a.name=='最大MP+20':
                自.MAXMP=自.MAXMP+20
            elif a.name=='ATK+2':
                自.atk=自.ATK+2
            elif a.name=='ATK+3':
                自.ATK=自.ATK+3
            elif a.name=='INT+2':
                自.INT=自.INT+2
            elif a.name=='INT+3':
                自.INT=自.INT+3
            elif a.name=='DEF+1':
                自.DEF=自.DEF+1
            elif a.name=='DEF+3':
                自.DEF=自.DEF+3
            if a.No>=0 and a.No<=9:
                アクティブスキル.append(a)
                アクティブスキル.sort(key=lambda x:x.No)
            else:
                パッシブスキル.append(a)
                パッシブスキル.sort(key=lambda x:x.No)
            習得済みスキル.remove(a)
            自.SP=自.SP-a.SP
            print()
        elif コマンド==2:
            print()

def スキル外し(a):
    print(a.name,'消費MP:',a.MP,'使用スキルスロット:',a.SP,'分類:',a.type)
    print(a.info)
    エラー処理=0
    while エラー処理==0:
        try:
            コマンド=-1
            コマンド=int(input('このスキルを外しますか？(1.はい 2.いいえ)'))
            if コマンド==1 or コマンド==2:
                エラー処理=1
            else:
                print('そんなコマンドはありません！')
        except ValueError:
            print('そんなコマンドはありません！') 
    if コマンド==1:
        print(自.name,'は',a.name,'を外した！')
        if a.name=='最大HP+10':
            自.MAXHP=自.MAXHP-10
            if 自.HP>自.MAXHP:
                自.HP=自.MAXHP
        elif a.name=='最大HP+20':
            自.MAXHP=自.MAXHP-20
            if 自.HP>自.MAXHP:
                自.HP=自.MAXHP
        elif a.name=='最大HP+50':
            自.MAXHP=自.MAXHP-50
            if 自.HP>自.MAXHP:
                自.HP=自.MAXHP
        elif a.name=='最大MP+10':
            自.MAXMP=自.MAXMP-10
        elif a.name=='最大MP+20':
            自.MAXMP=自.MAXMP-20
        elif a.name=='ATK+3':
            自.atk=自.ATK-3
        elif a.name=='atk+7':
            自.ATK=自.ATK-7
        elif a.name=='INT+3':
            自.INT=自.INT-3
        elif a.name=='INT+7':
            自.INT=自.INT-7
        elif a.name=='DEF+1':
            自.DEF=自.DEF-1
        elif a.name=='DEF+3':
            自.DEF=自.DEF-3
        習得済みスキル.append(a)
        習得済みスキル.sort(key=lambda x:x.No)
        if a.No>=0 and a.No<=9:
            アクティブスキル.remove(a)
        else:
            パッシブスキル.remove(a)
        自.SP=自.SP+a.SP
        print()
    elif コマンド==2:
        print()

class item:
    def __init__(self,name,所持数,買値,売値):
        self.name=name
        self.所持数=所持数
        self.買値=買値
        self.売値=買値
薬草=item('薬草',0,80,30)
ポーション=item('ポーション',0, 400,150)
聖水=item('聖水',0,120,50)
爆弾=item('爆弾',0,200,80)
スライムゼリー=item('スライムゼリー',0,1,20)#素材アイテムを買える場所は用意してないので買値は適当
ゴブリンの角=item('ゴブリンの角',0,1,60)
グリフォンの羽根=item('グリフォンの羽根',0,1,200)
霊結晶=item('霊結晶',0,1,1000)

#↓ここから各変数のセッティング
ゲーム終了=0
開発者モード=0
現在地='王都'
階層=[1]
未習得スキル=[S0,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11]
アクティブスキル=[]
パッシブスキル=[]
習得済みスキル=[]
所持金=[100]
消費アイテム一覧=['薬草','ポーション','聖水','爆弾','スキルの書']
消費アイテム=[0,0,0,0]
#アイテム名と呼び出し番号　0.薬草 1.聖水 2.爆弾
素材アイテム一覧=['スライムゼリー','ゴブリンの角','グリフォンの羽根']
素材アイテム=[0,0,0]
敵一覧=['スライム','ゴブリン','グリフォン']
コンティニュー=1
決定=2
コマンド=0
敵識別=0
脱出=0
エンカウント=0
イベント=0
入手数=0
エラー処理=0
#↓ここから関数周りのセッティング
def 戦闘処理(enemy):
    def ダメージ計算(a):
        ダメージぶれ=random.randint(int(a/5)*-1,int(a/5))
        与ダメ=a+ダメージぶれ-enemy.DEF
        if 与ダメ<=0:
            与ダメ=random.randint(0,1)
        return 与ダメ
    #↓ここから関数内関数によるスキル効果の設定 魔法についてはその仕様上関数にしない
    def 火炎切り():
        回避判定=0
        if 自.MP<=5:
            print('MPが足りない!')
        else:
            自.MP=自.MP-6
            print(自.name,'の 火炎切り !')
            与ダメ=int(ダメージ計算(int(自.ATK*2/3)+int(自.INT*2/3)))
            if enemy.name=='グリフォン':
                回避判定=random.randint(1,8)
            if 回避判定==1:
                print('しかし当たらなかった！')
            else:
                if 与ダメ>0:
                    print(enemy.name,'に',与ダメ,'のダメージ！')
                    enemy.HP=enemy.HP-与ダメ
                else:
                    print('しかしダメージを与えられなかった！')
    def 二連切り():
        回避判定=0
        if 自.MP<=5:
            print('MPが足りない！')
        else:
            自.MP=自.MP-6
            print(自.name,'の二連切り！')
            for i in range(2):
                与ダメ=int(ダメージ計算(自.ATK*3/4))
                if enemy.name=='グリフォン':
                    回避判定=random.randint(1,8)
                if 回避判定==1:
                    print('しかし当たらなかった！')
                else:
                    if 与ダメ>0:
                        print(enemy.name,'に',与ダメ,'のダメージ！')
                        enemy.HP=enemy.HP-与ダメ
                    else:
                        print('しかしダメージを与えられなかった！')
    def 貫通突き():
        回避判定=0
        if 自.MP<=4:
            print('MPが足りない！')
        else:
            自.MP=自.MP-5
            print(自.name,'の貫通突き！')
            与ダメ=int(ダメージ計算(自.ATK*0.8+enemy.DEF))
            if enemy.name=='グリフォン':
                回避判定=random.randint(1,8)
            if 回避判定==1:
                print('しかし当たらなかった！')
            else:
                if 与ダメ>0:
                    print(enemy.name,'に',与ダメ,'のダメージ！')
                    enemy.HP=enemy.HP-与ダメ
                else:
                    print('しかしダメージを与えられなかった！')
        
    #↓ここから戦闘関連の初期処理
    enemy.HP=enemy.MAXHP
    #elif 敵=='ボス':
    #    敵HP=ボスステータス[0]
    #    敵攻撃力=ボスステータス[1]
    #    敵防御力=ボスステータス[2]
    #    敵EXP=ボスステータス[3]
    戦闘終了=0
    敵討伐=0
    回避判定=0
    逃走判定=0
    ファイアボール=0
    ウィンドバレット=0
    サンダーボルト=0
    ATK強化小=0
    ATK上昇量小=0
    INT強化小=0
    INT上昇量小=0
    逃げ足=0
    防御=0
    根性=0
    聖水=0
    ターン=1
    ターン終了=1
    print(enemy.name,'があらわれた！')
    #↓ここからパッシブスキルの発動処理
    if S10 in パッシブスキル:
        根性=1
        print('パッシブスキル「根性」発動中！')
    if S11 in パッシブスキル:
        逃げ足=1
        print('パッシブスキル「逃げ足」発動中！')
    #↓ここから戦闘処理　終了条件:どちらかのHPが0以下、逃走にまだ成功していない
    while 戦闘終了==0:
        #↓一定ターン継続するスキルの処理
        if 防御>0:
            防御=防御-1
            if 防御==0:
                print(自.name,'は 構えを解いた！')
        if ATK強化小>=1:
            ATK強化小=ATK強化小-1
            if ATK強化小==0:
                print('ATK強化(小)の効果が切れた！')
                自.ATK=自.ATK-ATK上昇量小
        if INT強化小>=1:
            INT強化小=INT強化小-1
            if INT強化小==0:
                print('INT強化(小)の効果が切れた！')
                自.INT=自.INT-INT上昇量小
        ターン終了=0
        自.MP=自.MAXMP
        if 聖水>0:
            聖水=聖水-1
            自.MP=自.MP+int(自.MAXMP/2)
            if 聖水==0:
                print('聖水の効果が切れた！')
        while ターン終了==0:#特技等は何回でも使用可能
            print(ターン,'ターン目')
            print()
            print(自.name)
            print('HP',自.HP)
            print('MP',自.MP)
            if 防御>=1:
                print('防御中(あと',防御,'ターン持続)')
            if ATK強化小>=1:
                print('ATK強化(小)発動中(あと',ATK強化小,'ターン持続)')
            if INT強化小>=1:
                print('INT強化(小)発動中(あと',INT強化小,'ターン持続)')
            print()
            print('コマンド: 1.たたかう　2.防御　3.スキル　4.アイテム　5.ステータス確認　6.逃げる')
            エラー処理=0
            while エラー処理==0:
                try:
                    コマンド=-1
                    コマンド=int(input('コマンド選択:'))
                    if コマンド>=1 and コマンド<=6:
                        print()
                        エラー処理=1
                    else:
                        print('そんなコマンドはありません！')
                except ValueError:
                    print('そんなコマンドはありません！')
            if コマンド==1:#通常攻撃(ターン消費あり)
                print(自.name,'の攻撃！')
                与ダメ=ダメージ計算(自.ATK)
                if enemy.name=='グリフォン':
                    回避判定=random.randint(1,4)
                if 回避判定==1:
                    print('しかし当たらなかった！')
                else:
                    if 与ダメ>0:
                        print(enemy.name,'に',与ダメ,'のダメージ！')
                        enemy.HP=enemy.HP-与ダメ
                    else:
                        print('しかしダメージを与えられなかった！')
                ターン終了=1
            elif コマンド==2:#防御(ターン消費あり)
                if 防御==0:
                    print(自.name,'は身構えた！')
                    防御=1
                    ターン終了=1
                else:
                    print(自.name,'は既に身構えている！')
            elif コマンド==3:#スキル(ターン消費なし)
                print('0 戻る')#選択肢表示
                for i in range(len(アクティブスキル)):
                    print(i+1,アクティブスキル[i].name)
                エラー処理=0
                while エラー処理==0:
                    try:
                        エラー処理=1
                        技選択=-1
                        技選択=int(input('使うスキルを選べ！:'))
                        if 技選択==0:#何もせず戻すので空白でOK
                            print()
                        else:
                            技選択=アクティブスキル[技選択-1].name#ここから各スキルの関数に飛ばす処理
                    except (ValueError,IndexError):
                        print('そんなコマンドはありません！')
                        エラー処理=0
                    if 技選択=='火炎切り':
                        火炎切り()
                    elif 技選択=='二連切り':
                        二連切り()
                    elif 技選択=='貫通突き':
                        貫通突き()
                    elif 技選択=='ファイアボール':
                        if 自.MP<=5:
                            print('MPが足りない！')
                        else:
                            自.MP=自.MP-6
                            print(自.name,'はファイアボールを唱えた！')
                            ファイアボール=ファイアボール+1
                    elif 技選択=='ウィンドバレット':
                        if 自.MP<=6:
                            print('MPが足りない！')
                        else:
                            自.MP=自.MP-7
                            print(自.name,'はウィンドバレットを唱えた！')
                            ウィンドバレット=ウィンドバレット+1
                    elif 技選択=='サンダーボルト':
                        if 自.MP<=5:
                            print('MPが足りない！')
                        else:
                            自.MP=自.MP-6
                            print(自.name,'はサンダーボルトを唱えた！')
                            サンダーボルト=サンダーボルト+1
                    elif 技選択=='ヒール':
                        if 自.MP<=4:
                            print('MPが足りない！')
                        else:
                            自.MP=自.MP-5
                            print(自.name,'はヒールを唱えた！')
                            元HP=自.HP
                            自HP=自.HP+自.INT*2
                            if 自.HP>自.MAXHP:
                                自.HP=自.MAXHP
                            print(自.name,'のHPが',自.HP-元HP,'回復した！')
                    elif 技選択=='ATK強化(小)':
                        if 自.MP<=4:
                            print('MPが足りない！')
                        else:
                            自.MP=自.MP-5
                            print(自.name,'はATK強化(小)を発動した！')
                            if ATK強化小>=1:
                                ATK強化小=3
                                print('ATK強化(小)の効果時間が延長された！')
                            else:
                                ATK上昇量小=int(自.ATK*0.2)
                                自.ATK=自.ATK+ATK上昇量小
                                ATK強化小=3
                                print(自.name,'のATKが上がった！')
                    elif 技選択=='INT強化(小)':
                        if 自.MP<=4:
                            print('MPが足りない！')
                        else:
                            自.MP=自.MP-5
                            print(自.name,'はINT強化(小)を発動した！')
                            if INT強化小>=1:
                                INT強化小=3
                                print('INT強化(小)の効果時間が延長された！')
                            else:
                                INT上昇量小=int(自.INT*0.2)
                                自.INT=自.INT+INT上昇量小
                                INT強化小=3
                                print(自.name,'のINTが上がった！')
                    elif 技選択=='防御態勢':
                        if 自.MP<=5:
                            print('MPが足りない！')
                        else:
                            自.MP=自.MP-6
                            if 防御==0:
                                print(自.name,'は防御を固めた！')
                                防御=3
                            elif 防御>=1:
                                print(自.name,'は構えなおした！')
            elif コマンド==4:#アイテム使用(ターン消費あり)
                ターン終了=1 
                選択肢=1
                アイテム選択=0
                print('0 戻る')
                for i in range(len(消費アイテム)):
                    if 消費アイテム[i]>0:
                        print(選択肢,消費アイテム一覧[i],'  ',消費アイテム[i],'個')#持っているアイテムだけ所持数と合わせて表示、見た目と合わせるためiとコマンド用の数字は分離
                        選択肢=選択肢+1
                エラー処理=0
                while エラー処理==0:
                    try:
                        コマンド=-1
                        エラー処理=1
                        コマンド=int(input('使うアイテムを選べ！:'))
                        if コマンド==0:#ここも空白でOK
                            print()
                        else:
                            選択肢=0#ここで一度リセットしておく(↓でのバグの原因になるため)
                            while not 選択肢==コマンド:#やってること:↑のやつのiをアイテム選択で代用しコマンドの数字と選択肢が合うまで続けかみ合った(=プレイヤーが選んだアイテム)ならアイテム選択に格納し終了
                                if 消費アイテム[アイテム選択]>0:
                                    選択肢=選択肢+1
                                if 選択肢==コマンド:
                                    アイテム選択=消費アイテム一覧[アイテム選択]
                                else:
                                    アイテム選択=アイテム選択+1
                    except (ValueError,IndexError):
                        print('そんなコマンドはありません！')
                        エラー処理=0
                if アイテム選択==0:
                    ターン終了=0
                elif アイテム選択=='薬草':
                    print(自.name,'は 薬草 を使った！')
                    消費アイテム[0]=消費アイテム[0]-1
                    元HP=自.HP
                    回復ぶれ=random.randint(-2,2)#ぶれ幅は10%くらい？
                    自.HP=自.HP+15+回復ぶれ
                    if 自.HP>自.MAXHP:
                        自.HP=自.MAXHP
                    回復量=自.HP-元HP
                    print(自.name,'のHPが',回復量,'回復した！')
                elif アイテム選択=='聖水':
                    print(自.name,'は 聖水 を使った！')
                    消費アイテム[1]=消費アイテム[1]-1
                    print('しばらくターン開始時のMP回復量が増えた！')
                    聖水=3
                elif アイテム選択=='爆弾':
                    print(自.name,'は 爆弾 を使った！')
                    消費アイテム[2]=消費アイテム[2]-1
                    与ダメ=int(enemy.MAXHP/3)
                    enemy.HP=enemy.HP-与ダメ
                    print(enemy.name,'に',与ダメ,'のダメージを与えた！')
                else:
                    print('そんなコマンドはありません！')
                    ターン終了=0
            elif コマンド==5:#ステータス確認(ターン消費なし)
                print(自.name,'のステータス')
                print('レベル',自.Lv)
                print('EXP',自.EXP)
                print('次のレベルまで',自.NEXTEXP)
                print('最大HP',自.MAXHP)
                print('最大MP',自.MAXMP)
                print('攻撃力',自.ATK)
                print('防御力',自.DEF)
                print('装備中のアクティブスキル')
                if len(アクティブスキル)==0:
                    print('なし')
                else:
                    for i in range(len(アクティブスキル)):
                        print(アクティブスキル[i].name)
                print('装備中のパッシブスキル')
                if len(パッシブスキル)==0:
                    print('なし')
                else:
                    for i in range(len(パッシブスキル)):
                        print(パッシブスキル[i].name)
                    
            elif コマンド==6:#逃げる(ターン消費あり、確率で失敗)
                逃走判定=random.randint(0,1)
                print(自.name,'は逃げ出した！')
                if 逃走判定==1 or 逃げ足==1:
                    print('うまく逃げきれた！')
                    戦闘終了=1
                else:
                    print('しかし回り込まれてしまった！')
                ターン終了=1
            else:
                print('そんなコマンドはありません！')
            if enemy.HP<=0:
                ターン終了=1
        while ファイアボール>0:#ここから各魔法の処理
            ファイアボール=ファイアボール-1
            print(自.name,'のファイアボールが発動！')
            与ダメ=int(ダメージ計算(自.INT*1.2))
            if 与ダメ>0:
                print(enemy.name,'に',与ダメ,'のダメージ！')
                enemy.HP=enemy.HP-与ダメ
            else:
                print('しかしダメージを与えられなかった！')
        while ウィンドバレット>0:
            ウィンドバレット=ウィンドバレット-1
            print(自.name,'のウィンドバレットが発動！')
            for i in range(3):
                与ダメ=int(ダメージ計算(自.INT/2))
                if 与ダメ>0:
                    print(enemy.name,'に',与ダメ,'のダメージ！')
                    enemy.HP=enemy.HP-与ダメ
                else:
                    print('しかしダメージを与えられなかった！')
        while サンダーボルト>0:
            サンダーボルト=サンダーボルト-1
            print(自.name,'のサンダーボルトが発動！')
            与ダメ=int(ダメージ計算(自.INT+enemy.DEF))
            if 与ダメ>0:
                print(enemy.name,'に',与ダメ,'のダメージ！')
                enemy.HP=enemy.HP-与ダメ
            else:
                print('しかしダメージを与えられなかった！')
        if enemy.HP>0 and 戦闘終了==0:#ここから相手ターンの処理
            print(enemy.name,'の攻撃！')
            ダメージぶれ=random.randint(-1,1)
            与ダメ=enemy.ATK+ダメージぶれ-自.DEF
            if 防御>=1:
                与ダメ=int(与ダメ/2)
            if 与ダメ>0:
                print(自.name,'に',与ダメ,'のダメージ！')
                自.HP=自.HP-与ダメ
            else:
                print('しかし',自.name,'は ダメージを受けなかった！')
            if 自.HP<=0:
                if 根性==1:
                    print(自.name,'は根性で踏みとどまった！')
                    自.HP=1
                    根性=0
                else:
                    print(自.name,'は力尽きた...')
                    戦闘終了=1
                    自.HP=0
                    敵討伐=-1
            ターン=ターン+1
        else:
            if enemy.HP<=0:
                print(enemy.name,'を倒した！')
                戦闘終了=1
                敵討伐=1
    自.ATK=自.ATK-ATK上昇量小
    自.INT=自.INT-INT上昇量小
    if 敵討伐==1:
        print('経験値を',enemy.EXP,'獲得！')
        自.NEXTEXP=自.NEXTEXP-enemy.EXP
        while 自.NEXTEXP<=0:
            print(自.name,'のレベルが上がった！')
            print('スキルスロットが 1 増えた！')
            自.SP=自.SP+1
            自.SS=自.SS+1
            余剰EXP=自.NEXTEXP*-1
            自.NEXTEXP=10
            if 自.Lv==2:
                print(自.name,'は',S12.name,'と',S15.name,'を習得した！')
                習得済みスキル.append(S12)
                習得済みスキル.append(S15)
                習得済みスキル.sort(key=lambda x:x.No)
            elif 自.Lv==4:
                print(自.name,'は',S17.name,'と',S19.name,'を習得した！')
                習得済みスキル.append(S17)
                習得済みスキル.append(S19)
                習得済みスキル.sort(key=lambda x:x.No)
            elif 自.Lv==5:
                print(自.name,'は',S21.name,'を習得した！')
                習得済みスキル.append(S21)
                習得済みスキル.sort(key=lambda x:x.No)
            elif 自.Lv==6:
                print(自.name,'は',S18.name,'と',S20.name,'を習得した！')
                習得済みスキル.append(S18)
                習得済みスキル.append(S20)
                習得済みスキル.sort(key=lambda x:x.No)
            elif 自.Lv==8:
                print(自.name,'は',S13.name,'を習得した！')
                習得済みスキル.append(S13)
                習得済みスキル.sort(key=lambda x:x.No)
            elif 自.Lv==10:
                print(自.name,'は',S16.name,'と',S22.name,'を習得した！')
                習得済みスキル.append(S16)
                習得済みスキル.append(S22)
                習得済みスキル.sort(key=lambda x:x.No)
            elif 自.Lv==12:
                print(自.name,'は',S14.name,'を習得した！')
                習得済みスキル.append(S14)
                習得済みスキル.sort(key=lambda x:x.No)
            for i in range(1,自.Lv):
                自.NEXTEXP=int(自.NEXTEXP*0.6+自.Lv*8)
            自.NEXTEXP=自.NEXTEXP-余剰EXP
            自.Lv=自.Lv+1
        if enemy.name=='スライム':
            ドロップ抽選=random.randint(1,2)
            if ドロップ抽選==1:
                print(自.name,'はスライムゼリーを手に入れた！')
                素材アイテム[0]=素材アイテム[0]+1
        elif enemy.name=='ゴブリン':
            ドロップ抽選=random.randint(1,2)
            if ドロップ抽選==1:
                print(自.name,'はゴブリンの角を手に入れた！')
                素材アイテム[1]=素材アイテム[1]+1
        elif enemy.name=='グリフォン':
            ドロップ抽選=random.randint(1,2)
            if ドロップ抽選==1:
                print(自.name,'はグリフォンの羽根を手に入れた！')
                素材アイテム[2]=素材アイテム[2]+1
    elif 敵討伐==0:
        階層[0]=階層[0]-1
        print()
    elif 敵討伐==-1:
        print()
#ここまでが戦闘処理関連
#ここからが本編
print('操作方法:末尾が▼の時はenterキーで進む。末尾が:の時は数字等で選択肢を入力。(例:1.はい 2.いいえ でいいえを選ぶなら２と入力。使いやすさから半角モード推奨)')
print()
print('王城にて・・・')


print('王様「よくぞ来てくれた、冒険者よ。そなた、名はなんと言う？」')

エラー処理=0
while エラー処理==0:
    try:
        自.name=input('名前を入力してください:')
    except ValueError:
        print('王様「む？すまぬ、よく聞こえなかった。もう一度教えてくれぬか？」')
    if 自.name=='開発者モード':
        if 開発者モード==0:
            print('開発者モードを起動します')
            未習得スキル.remove(S0)
            未習得スキル.remove(S1)
            未習得スキル.remove(S2)
            未習得スキル.remove(S3)
            未習得スキル.remove(S4)
            未習得スキル.remove(S5)
            未習得スキル.remove(S6)
            未習得スキル.remove(S7)
            未習得スキル.remove(S8)
            未習得スキル.remove(S9)
            未習得スキル.remove(S10)
            未習得スキル.remove(S11)
            アクティブスキル.append(S0)
            アクティブスキル.append(S1)
            アクティブスキル.append(S2)
            アクティブスキル.append(S3)
            アクティブスキル.append(S4)
            アクティブスキル.append(S5)
            アクティブスキル.append(S6)
            アクティブスキル.append(S7)
            アクティブスキル.append(S8)
            アクティブスキル.append(S9)
            パッシブスキル.append(S10)
            パッシブスキル.append(S11)
            パッシブスキル.append(S12)
            パッシブスキル.append(S13)
            パッシブスキル.append(S14)
            パッシブスキル.append(S15)
            パッシブスキル.append(S16)
            パッシブスキル.append(S17)
            パッシブスキル.append(S18)
            パッシブスキル.append(S19)
            パッシブスキル.append(S20)
            パッシブスキル.append(S21)
            パッシブスキル.append(S22)
            自.MAXHP=100
            自.HP=100
            自.MAXMP=40
            自.MP=40
            自.ATK=10
            自.INT=10
            自.DEF=5
            自.Lv=99
            自.NEXTEXP=9999
            自.SS=99
            自.SP=61
            開発者モード=1
            continue
        else:
            print('開発者モードを停止します')
            自.MAXHP=20
            自.HP=20
            自.MAXMP=10
            自.MP=10
            自.ATK=5
            自.INT=5
            自.DEF=1
            自.Lv=1
            自.NEXTEXP=10
            自.SS=3
            自.SP=3
            開発者モード=0
            未習得スキル.append(S0)
            未習得スキル.append(S1)
            未習得スキル.append(S2)
            未習得スキル.append(S3)
            未習得スキル.append(S4)
            未習得スキル.append(S5)
            未習得スキル.append(S6)
            未習得スキル.append(S7)
            未習得スキル.append(S8)
            未習得スキル.append(S9)
            未習得スキル.append(S10)
            未習得スキル.append(S11)
            アクティブスキル.remove(S0)
            アクティブスキル.remove(S1)
            アクティブスキル.remove(S2)
            アクティブスキル.remove(S3)
            アクティブスキル.remove(S4)
            アクティブスキル.remove(S5)
            アクティブスキル.remove(S6)
            アクティブスキル.remove(S7)
            アクティブスキル.remove(S8)
            アクティブスキル.remove(S9)
            パッシブスキル.remove(S10)
            パッシブスキル.remove(S11)
            パッシブスキル.remove(S12)
            パッシブスキル.remove(S13)
            パッシブスキル.remove(S14)
            パッシブスキル.remove(S15)
            パッシブスキル.remove(S16)
            パッシブスキル.remove(S17)
            パッシブスキル.remove(S18)
            パッシブスキル.remove(S19)
            パッシブスキル.remove(S20)
            パッシブスキル.remove(S21)
            パッシブスキル.remove(S22)
            continue
    try:
        print('王様「なるほど、',自.name,'というんじゃな？」')
        コマンド=int(input('(1.はい 2.いいえ):'))
        if コマンド==1:
            エラー処理=1
        else:
            print('王様「おや、聞き間違いかの？もう一度聞かせてくれ。」')
    except ValueError:
        print('王様「む、なんと言った？もう一度聞かせてくれ。」')
try:
    コマンド=input('王様「よかろう、それでは本題に入る。そなたには最近発見されたダンジョンを探索してもらいたい。」▼')
except ValueError:
    コマンド=0
try:
    コマンド=input('王様「最深部にはこの世の物とは思えぬほどの宝があるそうだ。それを持ち帰ってもらうのが目標となる。」▼')
except ValueError:
    コマンド=0
try:
    コマンド=input('王様「当然、何の手助けもせずダンジョンに放り込みはせん。我々としても支援は惜しまん。」▼')
except ValueError:
    コマンド=0
try:
    コマンド=input('王様「まず、拠点として街の宿屋を手配している。費用は気にせず自由に使ってくれて構わん。」▼')
except ValueError:
    コマンド=0
try:
    コマンド=input('王様「さらに、支度金として1000Gを支給する。ひとまずの準備には事足りるだろう。」▼')
except ValueError:
    コマンド=0
if 開発者モード==0:
    print('王様「最後に、こちらが所有するスキルの書を一つ進呈しよう。３種類から好きに選んでくれたまえ。」')
    エラー処理=0
    while エラー処理==0:
        try:
            コマンド=-1
            print('1.火炎切り　2.貫通突き　3.ファイアボール')
            コマンド=int(input('どのスキルの書をもらう？:'))
            if コマンド==1:
                print('火炎切り:魔法で剣に炎を宿し切りつけるスキル。ATK、INTの両方に影響を受け、一撃の威力が高い。')
                コマンド=int(input('このスキルにしますか？(1.はい 2.やっぱりやめる):'))
                if コマンド==1:
                    print(自.name,'は火炎切りを習得した！')
                    アクティブスキル.append(S0)
                    アクティブスキル.sort(key=lambda x:x.No)
                    未習得スキル.remove(S0)
                    自.SP=自.SP-2
                    エラー処理=1
                elif コマンド==2:
                    print()
                else:
                    print('そんなコマンドはありません！')
            elif コマンド==2:
                print('貫通突き:剣で鋭く刺し貫くスキル。相手の防御力を無視してダメージを与えることができる。')
                コマンド=int(input('このスキルにしますか？(1.はい 2.やっぱりやめる)'))
                if コマンド==1:
                    print(自.name,'は貫通突きを習得した！')
                    アクティブスキル.append(S2)
                    アクティブスキル.sort(key=lambda x:x.No)
                    未習得スキル.remove(S2)
                    自.SP=自.SP-2
                    エラー処理=1
                elif コマンド==2:
                    print()
                else:
                    print('そんなコマンドはありません！')
            elif コマンド==3:
                print('ファイアボール:魔法で火球を作り打ち出すスキル。魔法の単発高威力担当なので扱いやすい。')
                コマンド=int(input('このスキルにしますか？(1.はい 2.やっぱりやめる):'))
                if コマンド==1:
                    print(自.name,'はファイアボールを習得した！')
                    アクティブスキル.append(S3)
                    アクティブスキル.sort(key=lambda x:x.No)
                    未習得スキル.remove(S3)
                    自.SP=自.SP-2
                    エラー処理=1
                elif コマンド==2:
                    print()
                else:
                    print('そんなコマンドはありません！')
            else:
                print('そんなコマンドはありません！')
        except ValueError:
            print('そんなコマンドはありません！')
try:
    コマンド=input('王様「それでは！旅立て冒険者よ！勇気と希望を胸に！」▼')
except ValueError:
    コマンド=0
try:
    print()
    コマンド=input('TIPS:このゲームの目的は「ダンジョンに潜ってアイテムを集めて装備を整え、ダンジョン最深部に眠る宝物を手に入れること」です。▼')
except ValueError:
    コマンド=0
try:
    コマンド=input('     最初から最深部にたどり着くのは困難なため、無理せず途中で街に戻り手に入れたアイテムで自らを強化しましょう。▼')
except ValueError:
    コマンド=0
try:
    コマンド=input('     なお、宿屋の本棚に役立つ情報が書かれた冒険者手帳が置かれています。一度目を通しておくと良いでしょう。▼')
except ValueError:
    コマンド=0
while ゲーム終了==0:
    while 現在地=='王都':
        print('～王都イニティウム～')
        print('1.雑貨屋(準備中) 2.工房(準備中) 3.宿屋 4.ダンジョンに潜る')
        エラー処理=0
        while エラー処理==0:
            try:
                コマンド=-1
                コマンド=int(input('どこへ行こうか？'))
                if コマンド>=1 and コマンド<=4:
                    エラー処理=1
                    print()
                else:
                    print('そんなコマンドはありません！')
            except ValueError:
                print('そんなコマンドはありません！')
        if コマンド==1:
            現在地='雑貨屋'
        elif コマンド==2:
            現在地='工房'
        elif コマンド==3:
            現在地='宿屋'
        elif コマンド==4:
            エラー処理=0
            while エラー処理==0:
                try:
                    コマンド=-1
                    コマンド=int(input('始まりの洞窟 に入ります。よろしいですか？(1.はい 2.いいえ):'))
                    if コマンド==1 or コマンド==2:
                        print()
                        エラー処理=1
                    else:
                        print('そんなコマンドはありません！')
                except ValueError:
                    print('そんなコマンドはありません！')
            if コマンド==1:
                現在地='ダンジョン'
    while 現在地=='雑貨屋':#次ここから　アイテム売り買いの処理作成中
        print('～雑貨屋～')
        print('店主「いらっしゃいませ～」')
        エラー処理=0
        while エラー処理==0:
            try:
                コマンド=-1
                コマンド=int(input('どうしようか？(0.店を出る 1.アイテムを買う 2.アイテムを売る)'))
                if コマンド>=0 and コマンド<=2:
                    print()
                else:
                    print('そんなコマンドはありません！')
            except ValueError:
                print('そんなコマンドはありません！')
        if コマンド==0:
            print('店主「ありがとうございました～」')
            print()
            現在地='王都'
        elif コマンド==1:
            print('店主「なにかご入用ですか？」')
            print('1 薬草',薬草.買値)
            print('2 ライフポーション',薬草.買値)
        elif コマンド==2:
            
    while 現在地=='工房':
        print('～工房～')
        print('工房主「すまねぇ、まだ準備中なんだ。また後で来てくれや」')
        try:
            コマンド=input(自.name,'は仕方ないので引き返した ▼')
        except ValueError:
            コマンド=0
        print()
        現在地='王都'
    while 現在地=='宿屋':
        if 自.HP<=0:
            print('宿屋の主人「おや、気がつかれましたか。他の冒険者さんいわくダンジョンの中で倒れていたそうですよ」')
            print('宿屋の主人「ひとまず治療しておきましたので後は自由にしてもらってかまいません」')
            print('宿屋の主人「ただし！治療費はしっかり請求しますので次からは気を付けてくださいね！」')
            アドバイス=random.randint(1,4)
            if アドバイス==1:
                try:
                    コマンド=input('宿屋の主人「ちなみに、倒れる前に脱出して休めばタダなので時には無理せず引くのも重要ですよ」▼')
                except ValueError:
                    コマンド=0
            elif アドバイス==2:
                try:
                    コマンド=input('宿屋の主人「ちなみに、回復手段は足りていますか？雑貨屋さんでいくつか薬を買っておくと安心ですよ」▼')
                except ValueError:
                    コマンド=0
            elif アドバイス==3:
                try:
                    コマンド=input('宿屋の主人「ちなみに、防御の効果は侮れませんよ。スキルで攻撃したらあとは防御するのも一つの手です」▼')
                except ValueError:
                    コマンド=0
            elif アドバイス==4:
                try:
                    コマンド=input('宿屋の主人「ちなみに、戦い方が単調になっていませんか？いつもと違う戦い方に突破口が隠れているかもしれません」▼')
                except ValueError:
                    コマンド=0
            元HP=自.HP
            自.HP=自.MAXHP
            自.MP=自.MAXMP
            回復量=自.HP-元HP
            治療費=回復量*自.Lv
            支払額=所持金[0]
            所持金[0]=所持金[0]-治療費
            if 所持金[0]<0:
                所持金[0]=0
            支払額=支払額-所持金[0]
            print('治療費として',支払額,'G払った')
            print()
        print('～宿屋～')
        print('1.ゆっくり休む 2.装備とスキルの確認・変更(α版につき未実装) 3.本棚(システム関連)を見る 4.宿屋を出る')
        エラー処理=0
        while エラー処理==0:
            try:
                コマンド=-1
                コマンド=int(input('どうしようか？:'))
                if コマンド>=1 and コマンド<=4:
                    エラー処理=1
                    print()
                else:
                    print('そんなコマンドはありません！')
            except ValueError:
                print('そんなコマンドはありません！')
        if コマンド==1:
            print(自.name,'は休んで体調を整えた・・・。')
            print('HPとMPが全回復した！')
            自.HP=自.MAXHP
            自.MP=自.MAXMP
            print()
        elif コマンド==2:
            print('0.やっぱりやめる 1.装備品(未実装につき封印中) 2.スキル(実装したかったけど間に合わず)')
            エラー処理=0
            while エラー処理==0:
                try:
                    コマンド=-1
                    コマンド=int(input('どちらについて考える？:'))
                    if コマンド==0 or コマンド==2:
                        エラー処理=1
                    elif コマンド==1:
                        print('スミマセンまだ実装できてないです、そのうち追加します')
                    else:
                        print('そんなコマンドはありません！')
                except ValueError:
                    print('そんなコマンドはありません！')
            if コマンド==2:
                終了=0
                while 終了==0:
                    print('スキルスロット ',自.SP,'/',自.SS)
                    print('現在セット中のアクティブスキル')
                    if len(アクティブスキル)==0:
                        print('なし')
                    else:
                        for i in range(len(アクティブスキル)):
                            print(アクティブスキル[i].name)
                    print('現在セット中のパッシブスキル')
                    if len(パッシブスキル)==0:
                        print('なし')
                    else:
                        for i in range(len(パッシブスキル)):
                            print(パッシブスキル[i].name)
                    print('セットしていないスキル')
                    if len(習得済みスキル)==0:
                        print('なし')
                    else:
                        for i in range(len(習得済みスキル)):
                            print(習得済みスキル[i].name)
                    print()
                    print('0.戻る　1.スキルをセットする　2.スキルを外す')
                    エラー処理=0
                    while エラー処理==0:
                        try:
                            コマンド=-1
                            コマンド=int(input('どうしようか？:'))
                            if コマンド>=0 and コマンド<=2:
                                エラー処理=1
                            else:
                                print('そんなコマンドはありません！')
                        except ValueError:
                            print('そんなコマンドはありません！')
                    if コマンド==0:
                        終了=1
                    elif コマンド==1:
                        if len(習得済みスキル)==0:
                            print('セットできるスキルが無いようだ')
                        else:
                            エラー処理=0
                            print('習得済みスキル一覧')
                            for i in range(len(習得済みスキル)):
                                print(i+1,習得済みスキル[i].name)
                            while エラー処理==0:
                                try:
                                    コマンド=-1
                                    スキル選択=0
                                    コマンド=int(input('どのスキルをセットする？(0で戻る):'))
                                    if コマンド==0:
                                        print()
                                    else:
                                        スキル選択=習得済みスキル[コマンド-1]
                                        スキルセット(スキル選択)
                                    エラー処理=1
                                except (ValueError,IndexError):
                                    print('そんなコマンドはありません！')
                    elif コマンド==2:
                        print('0.戻る 1.アクティブスキル 2.パッシブスキル')
                        エラー処理=0
                        while エラー処理==0:
                            try:
                                コマンド=-1
                                コマンド=int(input('どちらのスキルを外す？:'))
                                if コマンド>=0 and コマンド<=2:
                                    エラー処理=1
                                else:
                                    print('そんなコマンドはありません！')
                            except ValueError:
                                print('そんなコマンドはありません！')
                        if コマンド==0:
                            print()
                        elif コマンド==1:
                            if len(アクティブスキル)==0:
                                print('セットしているアクティブスキルがない！')
                            else:
                                for i in range(len(アクティブスキル)):
                                    print(i+1,アクティブスキル[i].name)
                                スキル選択=0
                                エラー処理=0
                                while エラー処理==0:
                                    try:
                                        コマンド=-1
                                        コマンド=int(input('どのスキルを外す？(0で戻る):'))
                                        if コマンド==0:
                                            print()
                                        else:
                                            スキル選択=アクティブスキル[コマンド-1]
                                            スキル外し(スキル選択)
                                        エラー処理=1
                                    except (ValueError,IndexError):
                                        print('そんなコマンドはありません！')
                        elif コマンド==2:
                            if len(パッシブスキル)==0:
                                print('セットしているパッシブスキルがない！')
                            else:
                                for i in range(len(パッシブスキル)):
                                    print(i+1,パッシブスキル[i].name)
                                スキル選択=0
                                エラー処理=0
                                while エラー処理==0:
                                    try:
                                        コマンド=-1
                                        コマンド=int(input('どのスキルを外す？(0で戻る):'))
                                        if コマンド==0:
                                            print()
                                        else:
                                            スキル選択=パッシブスキル[コマンド-1]
                                            スキル外し(スキル選択)
                                        エラー処理=1
                                    except (ValueError,IndexError):
                                        print('そんなコマンドはありません！')
        elif コマンド==3:
            print('0.やっぱりやめる 1.冒険者手帳(各種TIPS) 2.冒険の書(セーブ,未実装)')
            エラー処理=0
            while エラー処理==0:
                try:
                    コマンド=int(input('どの本を手に取る？:'))
                    if コマンド>=0 and コマンド<=2:
                        エラー処理=1
                        print()
                    else:
                        print('そんなコマンドはありません！')
                except ValueError:
                    print('そんなコマンドはありません！')
            if コマンド==1:
                while not コマンド==0:
                    print('0.本を閉じる 1.この世界について 2.戦闘について　3.クラフトについて 4.強くなるには？')
                    try:
                        コマンド=int(input('どのページを読もうか？:'))
                    except ValueError:
                        print('そんなコマンドはありません！')
                    if コマンド==0:
                        print(自.name,'は冒険者手帳を本棚に戻した')
                        print()
                    elif コマンド==1:
                        print('「モンスターが蔓延り、冒険者が旅をするのが日常の世界。近年、あちこちにダンジョンが発見され始めた。」')
                        print('「ダンジョンにはモンスターがいる一方、素材になるものから宝物まで様々なものも見つかっている。」')
                        print('「また、ダンジョンの最奥にはこの世のものと思えぬほどの宝が眠っていると噂されている。」')
                        print()
                    elif コマンド==2:
                        print('「基本的にはターン制の戦闘で、攻撃・防御・アイテム使用・逃げる場合にターンが終了する。(例外アリ)」')
                        print('「しかし、必ず知っておくべき点が3つ存在する。」')
                        print('「ひとつ、スキルを使用してもターンが終了しない。MPが続く限り連続で行動できる。」')
                        print('「そのため、最初期は1ターン目にバフをかけ2ターン目で高威力のスキルを連打するという戦法が確立された。」')
                        print('「ふたつ、攻撃魔法は詠唱が必要であり、自分ターン終了時に詠唱していた全ての魔法が一斉に発動する。」')
                        print('「大量の魔法が一気に放たれる瞬間は魔法使いにとって最高のロマンだそうだ。また、詠唱中の魔法を使うスキルも存在するらしい。」')
                        print('「みっつ、MPは毎ターンの始めに全回復する。一部のスキルやアイテムを使えばそれ以上に回復することも可能だ。」')
                        print('「なのでMP切れは気にせず、ガンガン使い切る気で戦うべきだ。自分のMPに合わせてスキルを構築するのもいいだろう。」')
                        print('「これらの点から戦い方の自由度が非常に高い。まずは自分好みの戦法を探すところから始めよう。」')
                        print()
                    elif コマンド==3:
                        print('「ダンジョンで採集したものやモンスターから得た素材を使って別のアイテムを作ることができます。」')
                        print('「一例として、薬草とスライムゼリーを用いたポーションは薬草単体より効果が高いことで非常に有名ですね。」')
                        print('「ただし、武器・防具等の装備品は鍛冶の知識が必要になるため作れません。工房を頼りましょう。」')
                        print('「単に自分が使うものを作るだけにとどまらず、加工したものを売却して収入を得ることもできます。」')
                        print('「強さに直結はしませんが、行き詰った時はポーションの備蓄などを見直してはどうでしょう？」')
                        print()
                    elif コマンド==4:
                        print('「一口に強くなる方法といっても様々な方法がある。ここでは主な３つの例を教えよう。」')
                        print('「第一に、レベルを上げることだ。単純ではあるが、それゆえ最も重要と言っても過言ではない。」')
                        print('「レベルを上げればセットできるスキルが増え、ステータスを底上げするスキルも手に入る。より自由度が増すだろう。」')
                        print('「次に、セットするスキルの選別だ。これもレベルに並ぶ重要な部分だと言える。なにせスキルスロットは有限だからな。」')
                        print('「スキル構成は戦い方に直結するため、方向性を絞るべきだ。スキルとスキルの相乗効果も意識するとなおいい。」')
                        print('「最後にアイテムの活用だ。時には物に頼ることが最善であることもある。覚えておくように。」')
                        print('「時に回復、時に攻撃、時には自身の強化など、アイテムにできることは多い。一定の準備をしておくべきだ。」')
                        print('「他にもバフの活用や敵との相性などがあるが後回しでかまわない。ひとまずこの３つを意識してみてはどうだろうか？」')
                        print()
                    else:
                        print('そんなページはありません！')
            elif コマンド==2:
                print('体験版では利用できません()')
        elif コマンド==4:
            print()
            現在地='王都'
    while 現在地=='ダンジョン':
        print()
        print('～始まりの洞窟～')
        階層[0]=1
        脱出=0
        while 脱出==0:
            print('地下',階層[0],'階')
            エンカウント=random.randint(1,2)#エンカウント判定
            if 階層[0]==20:
                敵識別=リッチ
                戦闘処理(リッチ)
                if 自.HP>0:
                    print(自.name,'は')
            elif エンカウント<=1:
                敵識別=random.randint(1,8)#敵の抽選
                if 敵識別<=10-int(階層[0]):
                    敵識別=スライム
                elif 敵識別<=15-int(階層[0]):
                    敵識別=ゴブリン
                else:
                    敵識別=グリフォン
                戦闘処理(敵識別)
            else:
                イベント=random.randint(1,2)#発生イベントの抽選
                if イベント==1:
                    print('薬草が生えていた！')
                    入手数=random.randint(1,3)
                    print(自.name,'は薬草を',入手数,'個手に入れた！')
                    消費アイテム[0]=消費アイテム[0]+入手数
                elif イベント>=2:
                    try:
                        print(自.name,'は宝箱を見つけた！')
                        print('中には スキルの書 が入っていた！')
                        習得スキル=random.randint(0,len(未習得スキル)-1)
                        print(自.name,'は',未習得スキル[習得スキル].name,'を習得した！')
                        習得済みスキル.append(未習得スキル[習得スキル])
                        習得済みスキル.sort(key=lambda x:x.No)
                        未習得スキル.remove(未習得スキル[習得スキル])
                    except ValueError:
                        print('しかしこれ以上覚えられるスキルがなかった。よくそんなに集めたな？')
                #elif イベント==3:
                #    print('しかし この階には何もなかった')
            if 自.HP<=0:
                脱出=1
                現在地='宿屋'
            else:
                print('1.次の階に進む 2.ここで脱出する')
                エラー処理=0
                while エラー処理==0:
                    try:
                        コマンド=-1
                        コマンド=int(input('どうしようか？:'))
                    except ValueError:
                        print('そんなコマンドはありません！')
                    if コマンド==1 or コマンド==2:
                        エラー処理=1
                        print()
                    else:
                        print('そんなコマンドはありません！')
                if コマンド==1:
                    階層[0]=階層[0]+1
                elif コマンド==2:
                    print(自.name,'はダンジョンから脱出した！')
                    脱出=1
                    現在地='王都'
                
                        

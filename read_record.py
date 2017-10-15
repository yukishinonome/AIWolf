import glob
from collections import OrderedDict

if __name__ == '__main__':
    
    log_list = []
    result_list = []
    file_list = glob.glob('--dir--/log/*.log')

    for filename in file_list:
        with open(filename, 'r') as input:
            # ファイルから最後の２行を読み込む(自分の役職と結果の把握のため)
            f = input.readlines()[-2:]
            for i, log in enumerate(f):
                if i == 0:
                    log_list.append(log[:-1])
                else:
                    result_list.append(log[:-1])

    # print(log_list)
    # print(result_list)

    win = 0
    total = len(log_list)
    record_dic = OrderedDict([('VILLAGER', [0, 0]), ('SEER', [0, 0]), ('MEDIUM', [0, 0]), ('BODYGUARD', [0, 0]), ('POSSESSED', [0, 0]), ('WEREWOLF', [0, 0])])
    # カウント
    for l, r in zip(log_list, result_list):
        if l.split(',')[3] == 'VILLAGER':
            record_dic['VILLAGER'][1] += 1
            if r.split(',')[-1] == 'VILLAGER':
                record_dic['VILLAGER'][0] += 1
                win += 1
        elif l.split(',')[3] == 'SEER':
            record_dic['SEER'][1] += 1
            if r.split(',')[-1] == 'VILLAGER':
                record_dic['SEER'][0] += 1
                win += 1
        elif l.split(',')[3] == 'MEDIUM':
            record_dic['MEDIUM'][1] += 1
            if r.split(',')[-1] == 'VILLAGER':
                record_dic['MEDIUM'][0] += 1
                win += 1
        elif l.split(',')[3] == 'BODYGUARD':
            record_dic['BODYGUARD'][1] += 1
            if r.split(',')[-1] == 'VILLAGER':
                record_dic['BODYGUARD'][0] += 1
                win += 1
        elif l.split(',')[3] == 'POSSESSED':
            record_dic['POSSESSED'][1] += 1
            if r.split(',')[-1] == 'WEREWOLF':
                record_dic['POSSESSED'][0] += 1
                win += 1
        else:
            record_dic['WEREWOLF'][1] += 1
            if r.split(',')[-1] == 'WEREWOLF':
                record_dic['WEREWOLF'][0] += 1
                win +=1
            
    rate = 0
    for key, value in record_dic.items():
        if value[1] == 0:
            rate = 0
        else:
            rate = value[0] / value[1]
        # 役職 : 勝った回数 / 担当した回数 : 勝率
        print(key, ':', value[0], '/', value[1], ':', '{:.3f}'.format(rate))
    
    # print('win :', win)
    # print('total :', total)
    # 全体の勝率
    print('Total :', '{:.3f}'.format(win / total))

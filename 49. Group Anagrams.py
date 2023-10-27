
def isAnagram(x, y):
    for letter in set(x):
        if x.count(letter) != y.count(letter):
            return False
    return True

def groupAnagrams(strs):
    strs.sort(key=len)
    result_list = []
    r = 1
    while len(strs) > 0:
        intermediary_result = []
        intermediary_result.append(strs[0])
        while r < len(strs) and len(strs[0]) == len(strs[r]):
            if isAnagram(strs[0], strs[r]):
                intermediary_result.append(strs[r])
                del strs[r]
            else:
                r += 1
        result_list.append(intermediary_result)
        del strs[0]
        r = 1
    return result_list




if __name__ == '__main__':
    strs = ["sobbed","lolling","forester","mispronounce","little","bugger","jettison","hysterics","nightingale","transvestites","oates","purges","nonalcoholics","surpluses","wraith","prokofiev","fornicate","pharisee","writer","hydra","pleasured","alienation","ulcerous","kosygin","awarest","hawkish","brahmanisms","regretful","nifty","naivest","deliberates","architectures","undefinable","peloponnese","choirs","cooperation","photostat","misrepresenting","tuckers","ditch","milksops","dilbert","lesbianism","advertises","wordsworth","lavishes","disloyally","mongolians","arizonans","moistened","m","satirize","professorship","odom","overlong","dislodges","privileges","persians","dated","survivor","effie","informants","charming","termed","trendiest","disenchants","impressionable","squiggling","potshots","broods","adeline","cog","dunged","yang","slayings","llano","heathen","chatterley","lush","birthplace","alphabetizing","yucked","studs","spokespersons","overcoat","bubbly","liquids","referees","ostracized","levelled","salvation","conferred","shoeshines","bluenose","arbitrate","flatbeds","attempt","suavity","ombudsman","attributively","cheerful","vancouver","filliped","murdoch","pluralistic","tempests","enhancing","rostand","ebonies","chipped","bodice","causation","sharron","waxiness","lute","snoozes","dickered","gratifies","neuron","condemned","javelin","undisturbed","lauded","vetting","burrows","prolific","scarves","sorrowed","understatements","affabler","ampuls","malices","extemporizing"]

    print(groupAnagrams(strs))
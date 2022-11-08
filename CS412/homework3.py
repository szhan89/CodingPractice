def ord_prefixspan(file, minsup):
        data_file = open(file, 'r')
        seqList = []
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                seqList.append(line.split()[1].replace("<", "").replace(">", ""))
        
        def dfs(pattern,sequence,index):
            if index == len(sequence)+1:
                return
            if pattern != "":
                n[pattern] = 1
            for i in range(index,len(sequence)):
                dfs(pattern + sequence[i], sequence, i + 1)
            return 
        
        _map = {}
        for s in seqList:
            n = {}
            dfs("",s,0)
            for key in n:
                if key in _map:
                    _map[key] += n[key]
                else:
                    _map[key] = n[key]
                    
                    
        tmp = sorted(_map)
        res = {}
        for i in tmp:
            if _map[i] >= minsup:
                res[i] = _map[i]
        return res
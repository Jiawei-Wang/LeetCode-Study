# 3 methods:
# 1. put key value: put key value pair into DS
# 2. get key: return the newest value for the key, if not exist return none
# 3. get key version: return the value for the version that is <= given version number
class KVStore:
    def __init__(self):
        self.dic = dict()
        self.version = 0 # init as 0, first key value input will be of version 1
    
    def put(self, key, value):
        version = self.version + 1
        # check if key is already in dic
        if key in self.dic:
            self.dic[key].append([version, value])
        else:
            self.dic[key] = [[version, value]]
        self.version = version
        return "PUT #" + str(version) + " " + str(key) + '=' + str(value)
    
    def get(self, key):
        if key in self.dic:
            return "GET " + str(key) + " (#" + str(self.dic[key][-1][0]) + ')=' + str(self.dic[key][-1][1])
        else:
            return "GET " + str(key) + '=' + 'NULL'
    
    def getVer(self, key, version):

        def binarySearch(key, version): # find the version that is <= given version number and return the [version, value] record, or None if nothing found
            # allRecord = self.dic[key] # [[version1, value1], [version2, value2], [...]]
            
            # # use index for elements in allRecord
            # left = 0 
            # right = len(allRecord) - 1
            # while left < right:
            #     mid = left + (right-left)//2

            #     if allRecord[mid][0] == version:
            #         return allRecord[mid]
            #     elif allRecord[mid][0] > version:
            #         right = mid - 1
            #     else:
            #         left = mid
            #         if allRecord[right][0] < version:
            #             return allRecord[right]
            # if left != 0 or allRecord[left][0] < version:
            #     return allRecord[left]
            # else:
            #     return None
            allRecord = self.dic[key]
            for item in allRecord[::-1]:
                if item[0] <= version:
                    return item
            return None



        if key in self.dic:
            record = binarySearch(key, version) # two possible outcomes for this: 1. a solid [version, value] record, 2. no record eariler than given version
            if record:
                return "GET " + str(key) + ' #' + str(record[0]) + ' =' + str(record[1])
            else:
                return 'GET ' + str(key) + '=' + 'NULL'
        else: # if the key is not in dic, also return NUll
            return 'GET ' + str(key) + '=' + 'NULL'


                





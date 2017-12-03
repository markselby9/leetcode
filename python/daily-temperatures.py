class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        length = len(temperatures)
        if length < 1: return []
        if length == 1: return [0]

        record = [0 for i in range(length)]
        tempature_pos_map = [0 for i in range(101)] # (30 - 100)
        i = length - 1
        while i >= 0:
            tempature_pos_map[temperatures[i]] = i # temp -> pos

            if i == length - 1:
                record[i] = 0
            elif temperatures[i] < temperatures[i + 1]:
                record[i] = 1
            elif temperatures[i] == temperatures[i+1]:
                if record[i + 1] > 0:
                    record[i] = record[i + 1] + 1
                else:
                    record[i] = 0
            else: # >
                current_temperature = temperatures[i]
                search_temprature = current_temperature + 1
                candidate = 999999999999
                while search_temprature < 101:
                    if tempature_pos_map[search_temprature] > 0:
                        candidate = min(candidate, tempature_pos_map[search_temprature])
                    search_temprature += 1
                # print current_temperature, i, candidate, record
                if candidate == 999999999999: record[i] = 0
                else:
                    record[i] = candidate - i

            i -= 1

        return record

# print Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
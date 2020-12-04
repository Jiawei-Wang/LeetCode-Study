# 解法1: greedy + heap
# 基本思路: 挑选同一时间点最早即将结束的事件
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510262/Detailed-analysisLet-me-lead-you-to-the-solution-step-by-step

TODO: 并不是完全理解答案, 还需要再思考
import heapq

class Solution:
    def maxEvents(self, events):
        # sort according to start time
        events = sorted(events)
        
        # 总天数为events中所有事件的最迟结束日期
        total_days = max(event[1] for event in events)
        
        # 保存可选事件的结束日期
        min_heap = []
        
        # 初始化为第1天, 共参加0个会议, events下标在0
        day, cnt, event_id = 1, 0, 0
        
        while day <= total_days:
		    # if no events are available to attend today, let time flies to the next available event.
            if event_id < len(events) and not min_heap:
                day = events[event_id][0]
			
			# all events starting from today are newly available. add them to the heap.
            while event_id < len(events) and events[event_id][0] <= day:
                heapq.heappush(min_heap, events[event_id][1])
                event_id += 1

			# if the event at heap top already ended, then discard it.
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

			# attend the event that will end the earliest
            if min_heap:
                heapq.heappop(min_heap)
                cnt += 1
            elif event_id >= len(events):
                break  # no more events to attend. so stop early to save time.
            day += 1
        return cnt
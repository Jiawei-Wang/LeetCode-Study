class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # a task has 3 attributes:
        # 1. available_time: time stamp when it becomes available
        # 2. process_time: how long it takes to process this task
        # 3. task_label
        # at time stamp x, we want to pick all available tasks
        # by shortest process_time and smallest task_label

        # sort all tasks by:
        # 1 -> 2 -> 3
        todo = [] 
        for index in range(len(tasks)):
            task_label = index
            available_time = tasks[index][0]
            process_time = tasks[index][1]
            todo.append((available_time, process_time, task_label))
        heapq.heapify(todo)
        # for example tasks = [[1,2],[2,4],[3,2],[4,1]]
        # todo = [(1, 2, 0), (2, 4, 1), (3, 2, 2), (4, 1, 3)]
        # first available task is: time = 1, process = 2, task label = 0
        
        order = []
        current_time = 1

        wait = [] # heap to manage all available tasks, ordered by 2 -> 3
        heapq.heapify(wait)

        while todo or wait:
            # first find if any task in todo can be added to wait
            while todo and todo[0][0] <= current_time:
                new_task = heapq.heappop(todo)
                heapq.heappush(wait, (new_task[1], new_task[2])) 
            # then we pick one in wait to process
            if wait:
                first = heapq.heappop(wait)
                order.append(first[1])
                current_time += first[0]
            else:
                current_time = todo[0][0]

        return order
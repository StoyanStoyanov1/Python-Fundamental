class MinerTask:


    def __init__(self):
        self.all_resources = self.add_resources()


    def add_resources(self):
        all_resources = {}
        while True:
            current_resource = input()
            if current_resource == "stop":
                break
            current_value = int(input())
            if current_resource not in all_resources:
                all_resources[current_resource] = current_value
            else:
                all_resources[current_resource] += current_value

        return all_resources


    def __repr__(self):
        result = []
        for key, value in self.all_resources.items():
            result.append(f"{key} -> {value}")
        return "\n".join(result)


print(MinerTask())
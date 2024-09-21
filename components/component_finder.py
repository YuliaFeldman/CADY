from typing import List


class ComponentFinder:
    @staticmethod
    def find_operable_components(components, **conditions):
        operable_components = []
        for component, ranges in components.items():
            if all(ranges[range_type] and ranges[range_type][0] <= value <= ranges[range_type][1] for range_type, value in conditions.items()):
                operable_components.append(component)
        return operable_components

from components.components_manager import ComponentsManager


if __name__ == '__main__':
    components_manager = ComponentsManager()

    # Examples how to use the system
    print(components_manager.find_operable_components(5.5, -20))
    print(components_manager.find_operable_components(0, 0))
    print(components_manager.find_operable_components(1.8, 10.5))

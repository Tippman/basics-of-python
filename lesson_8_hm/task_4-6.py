class Warehouse:
    """Склад. Тут хранится инфа о всей технике"""
    __office_equipment_collection = {
        'printer': [],
        'scanner': [],
        'copier': []
    }
    __equipment_in_departments = {
        'accounts_department': [],
        'staff_department': []
    }

    @staticmethod
    def add_to_global_collection(eq_type, item):
        return Warehouse.__office_equipment_collection[eq_type].append(item)

    def get_full_qty(self):
        """Общее кол-во техники"""
        result = {}
        for eq_type in self.__office_equipment_collection:
            result[eq_type] = len(self.__office_equipment_collection[eq_type])
        return print(f"{'-' * 30}\nTotal quantity of the equipment:\n{result}")

    def get_reserved_qty(self):
        """Техника, закрепленная за подразделениями"""
        print(f"{'-' * 40}\nEquipment in the departments:")
        for department in self.__equipment_in_departments:
            printer_count = 0
            scanner_count = 0
            copier_count = 0
            for item in self.__equipment_in_departments[department]:
                if item['eq_type'] == 'printer':
                    printer_count += 1
                elif item['eq_type'] == 'scanner':
                    scanner_count += 1
                else:
                    copier_count += 1
            print(f"{department}: {printer_count} printer(s), {scanner_count} scanner(s), {copier_count} copier(s) ")

    def create_new_department(self, new_department_name):
        print(f"New department created: {new_department_name}")
        return self.__equipment_in_departments.update({new_department_name: []})

    def move_eq_to_department(self, department, obj):
        for eq_type in self.__office_equipment_collection:
            for j in self.__office_equipment_collection.get(eq_type):
                if obj.__dict__['serial_num'] == j['serial_num']:
                    print(f"{j['eq_type']} with S/N '{j['serial_num']}' moved in {department}")
                    self.__equipment_in_departments[department].append(j)
                    break


class OfficeEquip(Warehouse):
    def add_item(self):
        print(f"New equipment {self.__dict__} added in office equipment")
        return Warehouse.add_to_global_collection(self.__dict__['eq_type'], self.__dict__)


class Printer(OfficeEquip):
    def __init__(self, name, is_color, serial_num):
        self.name = name
        self.is_color = is_color
        try:
            self.serial_num = int(serial_num)
        except ValueError:
            print(f"Serial number of printer '{name}' must be integer")
        self.eq_type = 'printer'


class Scanner(OfficeEquip):
    def __init__(self, name, dpi, serial_num):
        self.name = name
        self.dpi = dpi
        self.serial_num = serial_num
        self.eq_type = 'scanner'


class Copier(OfficeEquip):
    def __init__(self, name, is_color, serial_num):
        self.name = name
        self.is_color = is_color
        self.serial_num = serial_num
        self.eq_type = 'copier'


main_warehouse = Warehouse()

p_1 = Printer(name="HP-4550", is_color=True, serial_num=12345)
OfficeEquip.add_item(p_1)
s_1 = Scanner(name="Canon", dpi=350, serial_num='x98-22')
OfficeEquip.add_item(s_1)
p_2 = Printer(name="Govnoprinter", is_color=False, serial_num=557799)
OfficeEquip.add_item(p_2)
c_1 = Copier(name="Xerox", is_color=False, serial_num='c-001-22')
OfficeEquip.add_item(c_1)

main_warehouse.move_eq_to_department("accounts_department", p_1)
main_warehouse.move_eq_to_department("accounts_department", s_1)
main_warehouse.move_eq_to_department("staff_department", p_2)

main_warehouse.create_new_department('new_dep')

main_warehouse.move_eq_to_department('new_dep', c_1)

main_warehouse.get_full_qty()

main_warehouse.get_reserved_qty()

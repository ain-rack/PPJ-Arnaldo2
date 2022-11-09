from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout

from datetime import datetime
from collections import OrderedDict
from utils.datatable import DataTable
from datetime import datetime
import mysql.connector

class AdminWindow(BoxLayout):        
    meses_tabela = OrderedDict()
    meses_tabela['mes'] = {}
    meses_tabela['total_de_vendas'] = {}
    meses_tabela['total_pago'] = {}
    meses_tabela['total_restante'] = {}

    janeiro_tabela = OrderedDict()
    fevereiro_tabela = OrderedDict()
    março_tabela = OrderedDict()
    abril_tabela = OrderedDict()
    maio_tabela = OrderedDict()
    junho_tabela = OrderedDict()
    julho_tabela = OrderedDict()
    agosto_tabela = OrderedDict()
    setembro_tabela = OrderedDict()
    outubro_tabela = OrderedDict()
    novembro_tabela = OrderedDict()
    dezembro_tabela = OrderedDict()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='arnaldo',
            passwd='senhasql1804',
            database='db_vinicius'
        )
        self.mycursor = self.mydb.cursor()

        scrn = self.ids.scrn_meses
        meses = self.get_meses()
        mesestable = DataTable(table=meses)
        scrn.add_widget(mesestable)

        cataguases_scrn = self.ids.tabela_cataguases
        cataguases = self.get_cataguases()
        cata_table = DataTable(table=cataguases)
        cataguases_scrn.add_widget(cata_table)

        mage_scrn = self.ids.tabela_mage
        mage = self.get_mage()
        mage_table = DataTable(table=mage)
        mage_scrn.add_widget(mage_table)


    def update_meses(self, meses, vendas, cobrado, restante):
        vendas = int(vendas)
        cobrado = int(cobrado)
        restante = int(restante)
        
        if meses == 'Janeiro':
            self.janeiro_tabela['total_de_vendas'] = vendas
            self.janeiro_tabela['total_pago'] = cobrado
            self.janeiro_tabela['total_restante'] = restante

            self.meses_tabela['total_de_vendas'] += self.janeiro_tabela['total_de_vendas']
            self.meses_tabela['total_pago'] += self.janeiro_tabela['total_cobrado']
            self.meses_tabela['total_restante'] += self.janeiro_tabela['total_restante']

            self.janeiro_tabela['total_de_vendas'].clear()
            self.janeiro_tabela['total_pago'].clear()
            self.janeiro_tabela['total_restante'].clear()

        elif meses == 'Fevereiro':
            self.fevereiro_tabela['total_de_vendas'] = vendas
            self.fevereiro_tabela['total_pago'] = cobrado
            self.fevereiro_tabela['total_restante'] = restante

        elif meses == 'Março':
            self.março_tabela['total_de_vendas'] = vendas
            self.março_tabela['total_pago'] = cobrado
            self.março_tabela['total_restante'] = restante

        elif meses == 'Abril':
            self.abril_tabela['total_de_vendas'] = vendas
            self.abril_tabela['total_pago'] = cobrado
            self.abril_tabela['total_restante'] = restante

        elif meses == 'Maio':
            self.maio_tabela['total_de_vendas'] = vendas
            self.maio_tabela['total_pago'] = cobrado
            self.maio_tabela['total_restante'] = restante

        elif meses == 'Junho':
            self.junho_tabela['total_de_vendas'] = vendas
            self.junho_tabela['total_pago'] = cobrado
            self.junho_tabela['total_restante'] = restante
        
        elif meses == 'Julho':
            self.julho_tabela['total_de_vendas'] = vendas
            self.julho_tabela['total_pago'] = cobrado
            self.julho_tabela['total_restante'] = restante

        elif meses == 'Agosto':
            self.agosto_tabela['total_de_vendas'] = vendas
            self.agosto_tabela['total_pago'] = cobrado
            self.agosto_tabela['total_restante'] = restante

        elif meses == 'Setembro':
            self.setembro_tabela['total_de_vendas'] = vendas
            self.setembro_tabela['total_pago'] = cobrado
            self.setembro_tabela['total_restante'] = restante

        elif meses == 'Outubro':
            self.outubro_tabela['total_de_vendas'] = vendas
            self.outubro_tabela['total_pago'] = cobrado
            self.outubro_tabela['total_restante'] = restante

        elif meses == 'Novembro':
            self.novembro_tabela['total_de_vendas'] = vendas
            self.novembro_tabela['total_pago'] = cobrado
            self.novembro_tabela['total_restante'] = restante

            self.meses_tabela['total_de_vendas'] += self.novembro_tabela['total_de_vendas']
            self.meses_tabela['total_pago'] += self.novembro_tabela['total_pago']
            self.meses_tabela['total_restante'] += self.novembro_tabela['total_restante']

            self.novembro_tabela.clear()

        else:
            self.dezembro_tabela['total_de_vendas'] = vendas
            self.dezembro_tabela['total_pago'] = cobrado
            self.dezembro_tabela['total_restante'] = restante

        content = self.ids.scrn_meses
        content.clear_widgets()
        sql = 'UPDATE tlb_mes SET meses=%s, total_vendas=%s,total_cobrado=%s,total_restante=%s WHERE meses=%s'
        values =[meses, self.meses_tabela['total_de_vendas'], self.meses_tabela['total_pago'], self.meses_tabela['total_restante'], meses]
        self.mycursor.execute(sql,values)
        self.mydb.commit()

        meses_tab = self.get_meses()
        userstable = DataTable(table=meses_tab)
        content.add_widget(userstable)


    def get_meses(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='arnaldo',
            password='senhasql1804',
            database='db_vinicius'
        )
        mycursor = mydb.cursor()
        _meses = OrderedDict()
        _meses['Meses'] = {}
        _meses['Total de Vendas'] = {}
        _meses['Total Cobrado'] = {}
        _meses['Total Restante'] = {}
        _meses['Ano'] = {}

        tot_meses = []
        tot_vendas = []
        tot_cobrado = []
        tot_restante = []
        tot_ano = []

        sql = 'SELECT * FROM tlb_mes'
        mycursor.execute(sql)
        meses = mycursor.fetchall()
        for mes in meses:
            tot_meses.append(mes[1])
            tot_vendas.append(mes[2])
            tot_cobrado.append(mes[3])
            tot_restante.append(mes[4])
            tot_ano.append(mes[5])
        length = len(meses)
        idx = 0
        while idx < length:
            _meses['Meses'][idx] = tot_meses[idx]
            _meses['Total de Vendas'][idx] = tot_vendas[idx]
            _meses['Total Cobrado'][idx] = tot_cobrado[idx]
            _meses['Total Restante'][idx] = tot_restante[idx]
            _meses['Ano'][idx] = tot_ano[idx]

            idx += 1
        return _meses


    def get_cataguases(self):
            mydb = mysql.connector.connect(
                host='localhost',
                user='arnaldo',
                password='senhasql1804',
                database='db_vinicius'
            )
            mycursor = mydb.cursor()
            _pracas = OrderedDict()
            _pracas['Vendedora'] = {}
            _pracas['Total de Vendas'] = {}
            _pracas['Total Cobrado'] = {}
            _pracas['Total Restante'] = {}
            _pracas['Mês'] = {}
            _pracas['Ano'] = {}
            vendedora = []
            total_vendas = []
            total_cobrado = []
            total_restante = []
            mes = []
            ano = []

            sql = 'SELECT * FROM tlb_cataguases'
            mycursor.execute(sql)
            pracas = mycursor.fetchall()
            for praca in pracas:
                vendedora.append(praca[1])
                total_vendas.append(praca[2])
                total_cobrado.append(praca[3])
                total_restante.append(praca[4])
                mes.append(praca[5])
                ano.append(praca[6])
            pracas_length = len(pracas)
            idx = 0
            while idx < pracas_length:
                _pracas['Vendedora'][idx] = vendedora[idx]
                _pracas['Total de Vendas'][idx] = total_vendas[idx]
                _pracas['Total Cobrado'][idx] = total_cobrado[idx]
                _pracas['Total Restante'][idx] = total_restante[idx]
                _pracas['Mês'][idx] = mes[idx]
                _pracas['Ano'][idx] = ano[idx]

                idx += 1

            return _pracas

    def add_vend_fields(self):
        data_mes = datetime.today()
        mes_num = data_mes.month
        ano_num = data_mes.year

        Meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
        mes = Meses[mes_num - 1]

        target = self.ids.ops_fields
        target.clear_widgets()
        crud_nome = TextInput(hint_text='Nome')
        crud_vendas = TextInput(hint_text='Total de Vendas')
        crud_cobra = TextInput(hint_text='Total Cobrado')
        crud_meses = Spinner(text=f'{mes}', values=['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro','Novembro', 'Dezembro'])
        crud_anos = Spinner(text=f'{ano_num}',values=['2022','2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'])
        crud_submit = Button(text='Adicionar',size_hint_x=None,width=100,on_release=lambda x: self.add_vend(crud_nome.text,crud_vendas.text,crud_cobra.text,crud_meses.text,crud_anos.text))

        target.add_widget(crud_nome)
        target.add_widget(crud_vendas)
        target.add_widget(crud_cobra)
        target.add_widget(crud_meses)
        target.add_widget(crud_anos)
        target.add_widget(crud_submit)


    def add_vend(self, nome,vendas,cobrado,meses,anos):
        content = self.ids.tabela_cataguases
        content.clear_widgets()
        restante = float(vendas) - float(cobrado)
        sql = 'INSERT INTO tlb_cataguases(revendedoras,total_vendas,total_cobrado,total_restante,mes,ano) VALUES(%s,%s,%s,%s,%s,%s)'
        values =[nome,vendas,cobrado,restante,meses,anos]

        self.mycursor.execute(sql,values)
        self.mydb.commit()

        cataguases = self.get_cataguases()
        userstable = DataTable(table=cataguases)
        content.add_widget(userstable)
        
        self.update_meses(meses,vendas,cobrado,restante)

    def update_vend_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
    
        data_mes = datetime.today()
        mes_num = data_mes.month
        ano_num = data_mes.year

        Meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
        mes = Meses[mes_num - 1]

        crud_nome = TextInput(hint_text='Nome')
        crud_vendas = TextInput(hint_text='Total de Vendas')
        crud_cobra = TextInput(hint_text='Total Cobrado')
        crud_meses = Spinner(text=f'{mes}', values=['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro','Novembro', 'Dezembro'])
        crud_anos = Spinner(text=f'{ano_num}',values=['2022','2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'])
        crud_submit = Button(text='Atualizar',size_hint_x=None,width=100,on_release=lambda x: self.update_vend(crud_nome.text,crud_vendas.text,crud_cobra.text,crud_meses.text,crud_anos.text))

        target.add_widget(crud_nome)
        target.add_widget(crud_vendas)
        target.add_widget(crud_cobra)
        target.add_widget(crud_meses)
        target.add_widget(crud_anos)
        target.add_widget(crud_submit)


    def update_vend(self, nome,vendas,cobrado,meses,anos):
        content = self.ids.tabela_cataguases
        content.clear_widgets()
        restante = float(vendas) - float(cobrado)
        sql = 'UPDATE tlb_cataguases SET revendedoras=%s, total_vendas=%s,total_cobrado=%s,total_restante=%s,mes=%s, ano=%s WHERE revendedoras=%s'
        values =[nome,vendas,cobrado,restante,meses,anos, nome]
        self.mycursor.execute(sql,values)
        self.mydb.commit()

        cataguases = self.get_cataguases()
        userstable = DataTable(table=cataguases)
        content.add_widget(userstable)


    def remove_vend_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_user = TextInput(hint_text='Vendedora')
        crud_submit = Button(text='Remover',size_hint_x=None,width=100,on_release=lambda x: self.remove_vend(crud_user.text))

        target.add_widget(crud_user)
        target.add_widget(crud_submit)


    def remove_vend(self,nome):
        content = self.ids.tabela_cataguases
        content.clear_widgets()

        sql = 'DELETE FROM tlb_cataguases WHERE revendedoras = %s'
        values = [nome]
        self.mycursor.execute(sql,values)
        self.mydb.commit()

        cataguases = self.get_cataguases()
        userstable = DataTable(table=cataguases)
        content.add_widget(userstable)

    
    def get_mage(self):
            mydb = mysql.connector.connect(
                host='localhost',
                user='arnaldo',
                password='senhasql1804',
                database='db_vinicius'
            )
            mycursor = mydb.cursor()
            _pracas = OrderedDict()
            _pracas['Vendedora'] = {}
            _pracas['Total de Vendas'] = {}
            _pracas['Total Cobrado'] = {}
            _pracas['Total Restante'] = {}

            vendedora = []
            total_vendas = []
            total_cobrado = []
            total_restante = []

            sql = 'SELECT * FROM tlb_mage'
            mycursor.execute(sql)
            pracas = mycursor.fetchall()
            for praca in pracas:
                vendedora.append(praca[1])
                total_vendas.append(praca[2])
                total_cobrado.append(praca[3])
                total_restante.append(praca[4])
            pracas_length = len(pracas)
            idx = 0
            while idx < pracas_length:
                _pracas['Vendedora'][idx] = vendedora[idx]
                _pracas['Total de Vendas'][idx] = total_vendas[idx]
                _pracas['Total Cobrado'][idx] = total_cobrado[idx]
                _pracas['Total Restante'][idx] = total_restante[idx]

                idx += 1

            return _pracas


    def change_screen(self, instance):
        if instance.text == 'Praças':
            self.ids.scrn_mngr.current = 'scrn_pracas_content'
        elif instance.text == 'Meses':
            self.ids.scrn_mngr.current = 'scrn_meses'
        elif instance.text == 'Cataguases':
            self.ids.scrn_mngr.current = 'scrn_cataguases'
        elif instance.text == 'Magé':
            self.ids.scrn_mngr.current = 'scrn_mage'


class AdminApp(App):
    def build(self):

        return AdminWindow()

if __name__=='__main__':
    AdminApp().run()
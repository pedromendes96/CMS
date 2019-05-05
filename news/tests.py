import json

from django.test import TestCase

from .parser import JsonHtmlParser


# Create your tests here.
class HTMLParserTestCase(TestCase):
    def setUp(self):
        pass

    def test_simple_html(self):
        """
        <div class="container">
          <div class="row">
            <div class="col-sm">
              One of three columns
            </div>
            <div class="col-sm">
              One of three columns
            </div>
            <div class="col-sm">
              One of three columns
            </div>
          </div>
        </div>
        """
        result = [
            {
                "tag": "div",
                "ATTRIBUTES": {
                    "class": "container"
                },
                "children": [
                    {
                        "tag": "div",
                        "ATTRIBUTES": {
                            "class": "row"
                        },
                        "children": [
                            {
                                "tag": "div",
                                "ATTRIBUTES": {
                                    "class": "col-sm"
                                },
                                "children": [

                                ],
                                "data": " One of three columns "
                            },
                            {
                                "tag": "div",
                                "ATTRIBUTES": {
                                    "class": "col-sm"
                                },
                                "children": [

                                ],
                                "data": " One of three columns "
                            },
                            {
                                "tag": "div",
                                "ATTRIBUTES": {
                                    "class": "col-sm"
                                },
                                "children": [

                                ],
                                "data": " One of three columns "
                            }
                        ],
                        "data": " "
                    }
                ],
                "data": " "
            }
        ]

        content = '<div class="container"> <div class="row"> <div class="col-sm"> One of three columns </div>' \
                  '<div class="col-sm"> One of three columns </div><div class="col-sm"> One of three columns </div>' \
                  '</div></div>'
        parser = JsonHtmlParser()
        parser.feed(content)
        print(parser.get_content())
        self.assertEqual(parser.get_content(), json.dumps(result))

    def test_complex_html(self):
        """
        <div class="td-portlet">
    <section class="portlet" id="portlet_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949">
        <div class="portlet-content">
            <div class="portlet-content-container" style="">
                <div class="portlet-body">
                    <div class="stats-viewer iter-widget iter-component iter-tabview" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_markupTabs">
                        <div id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949__aui_div" class="iter-tabview-content">
                            <ul class="iter-tabview-list iter-widget-hd" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList">
                                <li class="iter-tab first n1 odd iter-rankingtab-mostrecent-hd iter-widget iter-component iter-state-default iter-state-active iter-tab-active iter-state-hover" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList0li"><span id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList0span" class="iter-tab-content"><a class="iter-tab-label" href="javascript:;" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList0a">MAIS RECENTE</a></span> </li>
                                <li class="iter-tab n2 even iter-rankingtab-mostviewed-hd iter-widget iter-component iter-state-default" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList1li"><span id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList1span" class="iter-tab-content"><a class="iter-tab-label" href="javascript:;" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList1a">MAIS VISTO</a></span> </li>
                                <li class="iter-tab last n3 odd iter-rankingtab-mostcommented-hd iter-widget iter-component iter-state-default" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList2li"><span id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList2span" class="iter-tab-content"><a class="iter-tab-label" href="javascript:" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList2a">MAIS COMENTADO</a></span> </li>
                            </ul>
                            <div class="iter-tabview-content iter-widget-bd" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsContent">
                                <div class="iter-tabview-content-item   iter-tabview-content iter-widget-bd">
                                    <div class="element n1 odd first full-access iter-rankingtab-mostrecent-bd" iteridart="MD4476907"><span class="teaserItemPosition">1</span>
                                        <h3 class="template-19"> <div class="section small"><span class="assigned-section">Desporto </span></div> <a href="/desporto/arsenal-quebra-ciclo-de-13-jogos-sem-perder-do-manchester-united-MD4476907"> <h3 class="headline  font-1 extra-small bold"> <span class="priority-content" mlnid="idcon=2082293;order=1.0">Arsenal quebra ciclo de 13 jogos sem perder do Manchester United</span> </h3> </a>
                                        </h3>
                                    </div>
                                    <div class="element n2 even full-access iter-rankingtab-mostrecent-bd" iteridart="KD4476590"><span class="teaserItemPosition">2</span>
                                        <h3 class="template-19"> <div class="section small"><span class="assigned-section">Desporto </span></div> <a href="/desporto/dupla-de-arbitros-madeirenses-dirigiu-final-de-europeu-de-tenis-de-mesa-KD4476590"> <h3 class="headline  font-1 extra-small bold"> <span class="priority-content" mlnid="idcon=2082248;order=1.0">Dupla de árbitros madeirenses dirigiu final de Europeu de ténis de mesa</span> </h3> </a>
                                        </h3>
                                    </div>
                                    <div class="element n3 odd full-access iter-rankingtab-mostrecent-bd" iteridart="CD4476532"><span class="teaserItemPosition">3</span>
                                        <h3 class="template-19"> <div class="section small"><span class="assigned-section">Madeira </span></div> <a href="/madeira/joao-pedro-vieira-jose-quando-tiveres-candidata-e-lugar-entra-no-debate-sobre-as-eleicoes-europeias-ate-la-trabalha-CD4476532"> <h3 class="headline  font-1 extra-small bold"> <span class="priority-content" mlnid="idcon=2082226;order=2.0">João Pedro Vieira: “José, quando tiveres candidata e lugar, entra no debate sobre as Eleições Europeias. Até lá, trabalha...”</span> </h3> </a>
                                        </h3>
                                    </div>
                                    <div class="element n4 even full-access iter-rankingtab-mostrecent-bd" iteridart="DD4476489"><span class="teaserItemPosition">4</span>
                                        <h3 class="template-19"> <div class="section small"><span class="assigned-section">Desporto </span></div> <a href="/desporto/sebastien-ogier-vence-rali-do-mexico-e-aproxima-se-da-lideranca-do-mundial-DD4476489"> <h3 class="headline  font-1 extra-small bold"> <span class="priority-content" mlnid="idcon=2082216;order=1.0">Sébastien Ogier vence Rali do México e aproxima-se da liderança do Mundial</span> </h3> </a>
                                        </h3>
                                    </div>
                                    <div class="element n5 odd full-access iter-rankingtab-mostrecent-bd" iteridart="XD4476437"><span class="teaserItemPosition">5</span>
                                        <h3 class="template-19"> <div class="section small"><span class="assigned-section">Mundo </span></div> <a href="/mundo/trump-quer-canalizar-8-6-mil-milhoes-de-dolares-para-o-muro-no-proximo-orcamento-XD4476437"> <h3 class="headline  font-1 extra-small bold"> <span class="priority-content" mlnid="idcon=2082208;order=1.0">Trump quer canalizar 8,6 mil milhões de dólares para o muro no próximo orçamento</span> </h3> </a>
                                        </h3>
                                    </div>
                                    <div class="element n6 even last full-access iter-rankingtab-mostrecent-bd" iteridart="HD4476393"><span class="teaserItemPosition">6</span>
                                        <h3 class="template-19"> <div class="section small"><span class="assigned-section">Madeira </span></div> <a href="/madeira/antonio-costa-destaca-posicoes-ultraelegiveis-dos-candidatos-da-madeira-e-acores-HD4476393"> <h3 class="headline  font-1 extra-small bold"> <span class="priority-content" mlnid="idcon=2082170;order=1.0">António Costa destaca posições “ultraelegíveis” dos candidatos da Madeira e Açores</span> </h3> </a>
                                        </h3>
                                    </div>
                                </div>
                                <div class="iter-tabview-content-item  iter-helper-hidden iter-tabview-content iter-widget-bd">
                                    <div class="element n1 odd first full-access iter-rankingtab-mostviewed-bd" iteridart="NX4473197"><span class="teaserItemPosition">1</span>
                                        <h3 class="template-19">
<div class="section small"><span class="assigned-section">Casos do Dia </span></div>
<a href="/casos-do-dia/homem-vitima-de-paragem-no-funchal-acabou-por-morrer-NX4473197">
<h3 class="headline  font-1 extra-small bold">
<span class="priority-content" mlnid="idcon=2080914;order=1.0">Homem vítima de ‘paragem’ no Funchal acabou por morrer</span>
</h3>
                                        </a>
                                        </h3>
                                    </div>
                                    <div class="element n2 even full-access iter-rankingtab-mostviewed-bd" iteridart="CD4476307"><span class="teaserItemPosition">2</span>
                                        <h3 class="template-19">
<div class="section small"><span class="assigned-section">Casos do Dia </span></div>
<a href="/casos-do-dia/homem-vitima-de-overdose-no-bairro-de-santo-amaro-CD4476307">
<h3 class="headline  font-1 extra-small bold">
<span class="priority-content" mlnid="idcon=2082162;order=1.0">Homem vítima de overdose no Bairro de Santo Amaro</span>
</h3>
                                        </a>
                                        </h3>
                                    </div>
                                    <div class="element n3 odd full-access iter-rankingtab-mostviewed-bd" iteridart="YF4474643"><span class="teaserItemPosition">3</span>
                                        <h3 class="template-19">
<div class="section small"><span class="assigned-section">Casos do Dia </span></div>
<a href="/casos-do-dia/caes-recem-nascidos-atirados-para-uma-fazenda-em-camara-de-lobos-YF4474643">
<h3 class="headline  font-1 extra-small bold">
<span class="priority-content" mlnid="idcon=2081644;order=1.0">Cães recém-nascidos atirados para uma fazenda em Câmara de Lobos</span>
</h3>
                                        </a>
                                        </h3>
                                    </div>
                                    <div class="element n4 even full-access iter-rankingtab-mostviewed-bd" iteridart="HX4473238"><span class="teaserItemPosition">4</span>
                                        <h3 class="template-19">
<div class="section small"><span class="assigned-section">Desporto </span></div>
<a href="/desporto/guarda-redes-do-moreirense-partiu-o-braco-esquerdo-HX4473238">
<h3 class="headline  font-1 extra-small bold">
<span class="priority-content" mlnid="idcon=2080925;order=1.0">Guarda-redes do Moreirense partiu o braço esquerdo</span>
</h3>
                                        </a>
                                        </h3>
                                    </div>
                                    <div class="element n5 odd full-access iter-rankingtab-mostviewed-bd" iteridart="CF4474545"><span class="teaserItemPosition">5</span>
                                        <h3 class="template-19">
<div class="section small"><span class="assigned-section">Casos do Dia </span></div>
<a href="/casos-do-dia/homem-encontrado-morto-na-calheta-CF4474545">
<h3 class="headline  font-1 extra-small bold">
<span class="priority-content" mlnid="idcon=2081620;order=1.0">Homem encontrado morto na Calheta</span>
</h3>
                                        </a>
                                        </h3>
                                    </div>
                                    <div class="element n6 even last full-access iter-rankingtab-mostviewed-bd" iteridart="MY4472349"><span class="teaserItemPosition">6</span>
                                        <h3 class="template-19">
<div class="section small"><span class="assigned-section">Casos do Dia </span></div>
<a href="/casos-do-dia/bombeiros-e-emir-tentam-salvar-homem-no-funchal-MY4472349">
<h3 class="headline  font-1 extra-small bold">
<span class="priority-content" mlnid="idcon=2080760;order=1.0">Bombeiros e EMIR tentam salvar homem no Funchal</span>
</h3>
                                        </a>
                                        </h3>
                                    </div>
                                </div>
                                <div class="iter-tabview-content-item  iter-helper-hidden iter-tabview-content iter-widget-bd">
                                    <div class="element n1 odd first full-access iter-rankingtab-mostcommented-bd" iteridart="XA4471909"><span class="teaserItemPosition">1</span>
                                        <h3 class="template-19">
<div class="section small"><span class="assigned-section">Madeira </span></div>
<a href="/madeira/cdu-alerta-para-as-irregularidades-do-novo-hospital-privado-XA4471909">
<h3 class="headline  font-1 extra-small bold">
<span class="priority-content" mlnid="idcon=2080378;order=1.0">CDU alerta para as irregularidades do novo hospital privado</span>
</h3>
                                        </a>
                                        </h3>
                                    </div>
                                    <div class="element n2 even full-access iter-rankingtab-mostcommented-bd" iteridart="DA4471162"><span class="teaserItemPosition">2</span>
                                        <h3 class="template-19">
<div class="section small"><span class="assigned-section">País </span></div>
<a href="/pais/neto-de-moura-insiste-que-casos-de-violencia-domestica-nao-eram-particularmente-graves-DA4471162">
<h3 class="headline  font-1 extra-small bold">
<span class="priority-content" mlnid="idcon=2080237;order=1.0">Neto de Moura insiste que casos de violência doméstica não eram “particularmente graves”</span>
</h3>
                                        </a>
                                        </h3>
                                    </div>
                                    <div class="element n3 odd full-access iter-rankingtab-mostcommented-bd" iteridart="CF4474015"><span class="teaserItemPosition">3</span>
                                        <h3 class="template-19">
<div class="section small"><span class="assigned-section">Mundo </span></div>
<a href="/mundo/maduro-diz-que-novo-ataque-cibernetico-impediu-retorno-da-energia-CF4474015">
<h3 class="headline  font-1 extra-small bold">
<span class="priority-content" mlnid="idcon=2081123;order=1.0">Maduro diz que novo ataque “cibernético” impediu retorno da energia</span>
</h3>
                                        </a>
                                        </h3>
                                    </div>
                                    <div class="element n4 even full-access iter-rankingtab-mostcommented-bd" iteridart="DA4471764"><span class="teaserItemPosition">4</span>
                                        <h3 class="template-19">
<div class="section small"><span class="assigned-section">Madeira </span></div>
<a href="/madeira/assuncao-cristas-diz-que-a-sondagem-da-rua-esta-muito-animadora-para-o-cds-pp-DA4471764">
<h3 class="headline  font-1 extra-small bold">
<span class="priority-content" mlnid="idcon=2080354;order=1.0">Assunção Cristas diz que a “sondagem da rua” está “muito animadora” para o CDS-PP</span>
</h3>
                                        </a>
                                        </h3>
                                    </div>
                                    <div class="element n5 odd full-access iter-rankingtab-mostcommented-bd" iteridart="DB4470371"><span class="teaserItemPosition">5</span>
                                        <h3 class="template-19">
<div class="section small"><span class="assigned-section">Madeira </span></div>
<a href="/madeira/tragedia-do-monte-ensombra-eleicoes-DB4470371">
<h3 class="headline  font-1 extra-small bold">
<span class="priority-content" mlnid="idcon=2079710;order=1.0">Tragédia do Monte ensombra eleições</span>
</h3>
                                        </a>
                                        </h3>
                                    </div>
                                    <div class="element n6 even last full-access iter-rankingtab-mostcommented-bd" iteridart="FX4473362"><span class="teaserItemPosition">6</span>
                                        <h3 class="template-19">
<div class="section small"><span class="assigned-section">Madeira </span></div>
<a href="/madeira/jsd-quer-maior-proximidade-popular-e-aposta-na-vitoria-do-psd-nas-eleicoes-deste-ano-FX4473362">
<h3 class="headline  font-1 extra-small bold">
<span class="priority-content" mlnid="idcon=2080958;order=1.0">JSD quer maior proximidade popular e aposta na vitória do PSD nas eleições deste ano</span>
</h3>
                                        </a>
                                        </h3>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</div>
        :return:
        """
        content = '<div class="td-portlet"> <section class="portlet" id="portlet_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949"> <div class="portlet-content"> <div class="portlet-content-container" style=""> <div class="portlet-body"> <div class="stats-viewer iter-widget iter-component iter-tabview" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_markupTabs"> <div id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949__aui_div" class="iter-tabview-content"> <ul class="iter-tabview-list iter-widget-hd" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList"> <li class="iter-tab first n1 odd iter-rankingtab-mostrecent-hd iter-widget iter-component iter-state-default iter-state-active iter-tab-active iter-state-hover" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList0li"><span id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList0span" class="iter-tab-content"><a class="iter-tab-label" href="javascript:;" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList0a">MAIS RECENTE</a></span> </li><li class="iter-tab n2 even iter-rankingtab-mostviewed-hd iter-widget iter-component iter-state-default" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList1li"><span id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList1span" class="iter-tab-content"><a class="iter-tab-label" href="javascript:;" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList1a">MAIS VISTO</a></span> </li><li class="iter-tab last n3 odd iter-rankingtab-mostcommented-hd iter-widget iter-component iter-state-default" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList2li"><span id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList2span" class="iter-tab-content"><a class="iter-tab-label" href="javascript:" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList2a">MAIS COMENTADO</a></span> </li></ul> <div class="iter-tabview-content iter-widget-bd" id="_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsContent"> <div class="iter-tabview-content-item iter-tabview-content iter-widget-bd"> <div class="element n1 odd first full-access iter-rankingtab-mostrecent-bd" iteridart="MD4476907"><span class="teaserItemPosition">1</span> <h3 class="template-19"> <div class="section small"><span class="assigned-section">Desporto </span></div><a href="/desporto/arsenal-quebra-ciclo-de-13-jogos-sem-perder-do-manchester-united-MD4476907"> <h3 class="headline font-1 extra-small bold"> <span class="priority-content" mlnid="idcon=2082293;order=1.0">Arsenal quebra ciclo de 13 jogos sem perder do Manchester United</span> </h3> </a> </h3> </div><div class="element n2 even full-access iter-rankingtab-mostrecent-bd" iteridart="KD4476590"><span class="teaserItemPosition">2</span> <h3 class="template-19"> <div class="section small"><span class="assigned-section">Desporto </span></div><a href="/desporto/dupla-de-arbitros-madeirenses-dirigiu-final-de-europeu-de-tenis-de-mesa-KD4476590"> <h3 class="headline font-1 extra-small bold"> <span class="priority-content" mlnid="idcon=2082248;order=1.0">Dupla de árbitros madeirenses dirigiu final de Europeu de ténis de mesa</span> </h3> </a> </h3> </div><div class="element n3 odd full-access iter-rankingtab-mostrecent-bd" iteridart="CD4476532"><span class="teaserItemPosition">3</span> <h3 class="template-19"> <div class="section small"><span class="assigned-section">Madeira </span></div><a href="/madeira/joao-pedro-vieira-jose-quando-tiveres-candidata-e-lugar-entra-no-debate-sobre-as-eleicoes-europeias-ate-la-trabalha-CD4476532"> <h3 class="headline font-1 extra-small bold"> <span class="priority-content" mlnid="idcon=2082226;order=2.0">João Pedro Vieira: “José, quando tiveres candidata e lugar, entra no debate sobre as Eleições Europeias. Até lá, trabalha...”</span> </h3> </a> </h3> </div><div class="element n4 even full-access iter-rankingtab-mostrecent-bd" iteridart="DD4476489"><span class="teaserItemPosition">4</span> <h3 class="template-19"> <div class="section small"><span class="assigned-section">Desporto </span></div><a href="/desporto/sebastien-ogier-vence-rali-do-mexico-e-aproxima-se-da-lideranca-do-mundial-DD4476489"> <h3 class="headline font-1 extra-small bold"> <span class="priority-content" mlnid="idcon=2082216;order=1.0">Sébastien Ogier vence Rali do México e aproxima-se da liderança do Mundial</span> </h3> </a> </h3> </div><div class="element n5 odd full-access iter-rankingtab-mostrecent-bd" iteridart="XD4476437"><span class="teaserItemPosition">5</span> <h3 class="template-19"> <div class="section small"><span class="assigned-section">Mundo </span></div><a href="/mundo/trump-quer-canalizar-8-6-mil-milhoes-de-dolares-para-o-muro-no-proximo-orcamento-XD4476437"> <h3 class="headline font-1 extra-small bold"> <span class="priority-content" mlnid="idcon=2082208;order=1.0">Trump quer canalizar 8,6 mil milhões de dólares para o muro no próximo orçamento</span> </h3> </a> </h3> </div><div class="element n6 even last full-access iter-rankingtab-mostrecent-bd" iteridart="HD4476393"><span class="teaserItemPosition">6</span> <h3 class="template-19"> <div class="section small"><span class="assigned-section">Madeira </span></div><a href="/madeira/antonio-costa-destaca-posicoes-ultraelegiveis-dos-candidatos-da-madeira-e-acores-HD4476393"> <h3 class="headline font-1 extra-small bold"> <span class="priority-content" mlnid="idcon=2082170;order=1.0">António Costa destaca posições “ultraelegíveis” dos candidatos da Madeira e Açores</span> </h3> </a> </h3> </div></div><div class="iter-tabview-content-item iter-helper-hidden iter-tabview-content iter-widget-bd"> <div class="element n1 odd first full-access iter-rankingtab-mostviewed-bd" iteridart="NX4473197"><span class="teaserItemPosition">1</span> <h3 class="template-19"><div class="section small"><span class="assigned-section">Casos do Dia </span></div><a href="/casos-do-dia/homem-vitima-de-paragem-no-funchal-acabou-por-morrer-NX4473197"><h3 class="headline font-1 extra-small bold"><span class="priority-content" mlnid="idcon=2080914;order=1.0">Homem vítima de ‘paragem’ no Funchal acabou por morrer</span></h3> </a> </h3> </div><div class="element n2 even full-access iter-rankingtab-mostviewed-bd" iteridart="CD4476307"><span class="teaserItemPosition">2</span> <h3 class="template-19"><div class="section small"><span class="assigned-section">Casos do Dia </span></div><a href="/casos-do-dia/homem-vitima-de-overdose-no-bairro-de-santo-amaro-CD4476307"><h3 class="headline font-1 extra-small bold"><span class="priority-content" mlnid="idcon=2082162;order=1.0">Homem vítima de overdose no Bairro de Santo Amaro</span></h3> </a> </h3> </div><div class="element n3 odd full-access iter-rankingtab-mostviewed-bd" iteridart="YF4474643"><span class="teaserItemPosition">3</span> <h3 class="template-19"><div class="section small"><span class="assigned-section">Casos do Dia </span></div><a href="/casos-do-dia/caes-recem-nascidos-atirados-para-uma-fazenda-em-camara-de-lobos-YF4474643"><h3 class="headline font-1 extra-small bold"><span class="priority-content" mlnid="idcon=2081644;order=1.0">Cães recém-nascidos atirados para uma fazenda em Câmara de Lobos</span></h3> </a> </h3> </div><div class="element n4 even full-access iter-rankingtab-mostviewed-bd" iteridart="HX4473238"><span class="teaserItemPosition">4</span> <h3 class="template-19"><div class="section small"><span class="assigned-section">Desporto </span></div><a href="/desporto/guarda-redes-do-moreirense-partiu-o-braco-esquerdo-HX4473238"><h3 class="headline font-1 extra-small bold"><span class="priority-content" mlnid="idcon=2080925;order=1.0">Guarda-redes do Moreirense partiu o braço esquerdo</span></h3> </a> </h3> </div><div class="element n5 odd full-access iter-rankingtab-mostviewed-bd" iteridart="CF4474545"><span class="teaserItemPosition">5</span> <h3 class="template-19"><div class="section small"><span class="assigned-section">Casos do Dia </span></div><a href="/casos-do-dia/homem-encontrado-morto-na-calheta-CF4474545"><h3 class="headline font-1 extra-small bold"><span class="priority-content" mlnid="idcon=2081620;order=1.0">Homem encontrado morto na Calheta</span></h3> </a> </h3> </div><div class="element n6 even last full-access iter-rankingtab-mostviewed-bd" iteridart="MY4472349"><span class="teaserItemPosition">6</span> <h3 class="template-19"><div class="section small"><span class="assigned-section">Casos do Dia </span></div><a href="/casos-do-dia/bombeiros-e-emir-tentam-salvar-homem-no-funchal-MY4472349"><h3 class="headline font-1 extra-small bold"><span class="priority-content" mlnid="idcon=2080760;order=1.0">Bombeiros e EMIR tentam salvar homem no Funchal</span></h3> </a> </h3> </div></div><div class="iter-tabview-content-item iter-helper-hidden iter-tabview-content iter-widget-bd"> <div class="element n1 odd first full-access iter-rankingtab-mostcommented-bd" iteridart="XA4471909"><span class="teaserItemPosition">1</span> <h3 class="template-19"><div class="section small"><span class="assigned-section">Madeira </span></div><a href="/madeira/cdu-alerta-para-as-irregularidades-do-novo-hospital-privado-XA4471909"><h3 class="headline font-1 extra-small bold"><span class="priority-content" mlnid="idcon=2080378;order=1.0">CDU alerta para as irregularidades do novo hospital privado</span></h3> </a> </h3> </div><div class="element n2 even full-access iter-rankingtab-mostcommented-bd" iteridart="DA4471162"><span class="teaserItemPosition">2</span> <h3 class="template-19"><div class="section small"><span class="assigned-section">País </span></div><a href="/pais/neto-de-moura-insiste-que-casos-de-violencia-domestica-nao-eram-particularmente-graves-DA4471162"><h3 class="headline font-1 extra-small bold"><span class="priority-content" mlnid="idcon=2080237;order=1.0">Neto de Moura insiste que casos de violência doméstica não eram “particularmente graves”</span></h3> </a> </h3> </div><div class="element n3 odd full-access iter-rankingtab-mostcommented-bd" iteridart="CF4474015"><span class="teaserItemPosition">3</span> <h3 class="template-19"><div class="section small"><span class="assigned-section">Mundo </span></div><a href="/mundo/maduro-diz-que-novo-ataque-cibernetico-impediu-retorno-da-energia-CF4474015"><h3 class="headline font-1 extra-small bold"><span class="priority-content" mlnid="idcon=2081123;order=1.0">Maduro diz que novo ataque “cibernético” impediu retorno da energia</span></h3> </a> </h3> </div><div class="element n4 even full-access iter-rankingtab-mostcommented-bd" iteridart="DA4471764"><span class="teaserItemPosition">4</span> <h3 class="template-19"><div class="section small"><span class="assigned-section">Madeira </span></div><a href="/madeira/assuncao-cristas-diz-que-a-sondagem-da-rua-esta-muito-animadora-para-o-cds-pp-DA4471764"><h3 class="headline font-1 extra-small bold"><span class="priority-content" mlnid="idcon=2080354;order=1.0">Assunção Cristas diz que a “sondagem da rua” está “muito animadora” para o CDS-PP</span></h3> </a> </h3> </div><div class="element n5 odd full-access iter-rankingtab-mostcommented-bd" iteridart="DB4470371"><span class="teaserItemPosition">5</span> <h3 class="template-19"><div class="section small"><span class="assigned-section">Madeira </span></div><a href="/madeira/tragedia-do-monte-ensombra-eleicoes-DB4470371"><h3 class="headline font-1 extra-small bold"><span class="priority-content" mlnid="idcon=2079710;order=1.0">Tragédia do Monte ensombra eleições</span></h3> </a> </h3> </div><div class="element n6 even last full-access iter-rankingtab-mostcommented-bd" iteridart="FX4473362"><span class="teaserItemPosition">6</span> <h3 class="template-19"><div class="section small"><span class="assigned-section">Madeira </span></div><a href="/madeira/jsd-quer-maior-proximidade-popular-e-aposta-na-vitoria-do-psd-nas-eleicoes-deste-ano-FX4473362"><h3 class="headline font-1 extra-small bold"><span class="priority-content" mlnid="idcon=2080958;order=1.0">JSD quer maior proximidade popular e aposta na vitória do PSD nas eleições deste ano</span></h3> </a> </h3> </div></div></div></div></div></div></div></div></section></div>'
        result = [
   {
      "tag":"div",
      "ATTRIBUTES":{
         "class":"td-portlet"
      },
      "children":[
         {
            "tag":"section",
            "ATTRIBUTES":{
               "class":"portlet",
               "id":"portlet_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949"
            },
            "children":[
               {
                  "tag":"div",
                  "ATTRIBUTES":{
                     "class":"portlet-content"
                  },
                  "children":[
                     {
                        "tag":"div",
                        "ATTRIBUTES":{
                           "class":"portlet-content-container",
                           "style":""
                        },
                        "children":[
                           {
                              "tag":"div",
                              "ATTRIBUTES":{
                                 "class":"portlet-body"
                              },
                              "children":[
                                 {
                                    "tag":"div",
                                    "ATTRIBUTES":{
                                       "class":"stats-viewer iter-widget iter-component iter-tabview",
                                       "id":"_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_markupTabs"
                                    },
                                    "children":[
                                       {
                                          "tag":"div",
                                          "ATTRIBUTES":{
                                             "id":"_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949__aui_div",
                                             "class":"iter-tabview-content"
                                          },
                                          "children":[
                                             {
                                                "tag":"ul",
                                                "ATTRIBUTES":{
                                                   "class":"iter-tabview-list iter-widget-hd",
                                                   "id":"_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList"
                                                },
                                                "children":[
                                                   {
                                                      "tag":"li",
                                                      "ATTRIBUTES":{
                                                         "class":"iter-tab first n1 odd iter-rankingtab-mostrecent-hd iter-widget iter-component iter-state-default iter-state-active iter-tab-active iter-state-hover",
                                                         "id":"_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList0li"
                                                      },
                                                      "children":[
                                                         {
                                                            "tag":"span",
                                                            "ATTRIBUTES":{
                                                               "id":"_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList0span",
                                                               "class":"iter-tab-content"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"a",
                                                                  "ATTRIBUTES":{
                                                                     "class":"iter-tab-label",
                                                                     "href":"javascript:;",
                                                                     "id":"_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList0a"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"MAIS RECENTE"
                                                               }
                                                            ],
                                                            "data":""
                                                         }
                                                      ],
                                                      "data":" "
                                                   },
                                                   {
                                                      "tag":"li",
                                                      "ATTRIBUTES":{
                                                         "class":"iter-tab n2 even iter-rankingtab-mostviewed-hd iter-widget iter-component iter-state-default",
                                                         "id":"_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList1li"
                                                      },
                                                      "children":[
                                                         {
                                                            "tag":"span",
                                                            "ATTRIBUTES":{
                                                               "id":"_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList1span",
                                                               "class":"iter-tab-content"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"a",
                                                                  "ATTRIBUTES":{
                                                                     "class":"iter-tab-label",
                                                                     "href":"javascript:;",
                                                                     "id":"_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList1a"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"MAIS VISTO"
                                                               }
                                                            ],
                                                            "data":""
                                                         }
                                                      ],
                                                      "data":" "
                                                   },
                                                   {
                                                      "tag":"li",
                                                      "ATTRIBUTES":{
                                                         "class":"iter-tab last n3 odd iter-rankingtab-mostcommented-hd iter-widget iter-component iter-state-default",
                                                         "id":"_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList2li"
                                                      },
                                                      "children":[
                                                         {
                                                            "tag":"span",
                                                            "ATTRIBUTES":{
                                                               "id":"_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList2span",
                                                               "class":"iter-tab-content"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"a",
                                                                  "ATTRIBUTES":{
                                                                     "class":"iter-tab-label",
                                                                     "href":"javascript:",
                                                                     "id":"_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsList2a"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"MAIS COMENTADO"
                                                               }
                                                            ],
                                                            "data":""
                                                         }
                                                      ],
                                                      "data":" "
                                                   }
                                                ],
                                                "data":" "
                                             },
                                             {
                                                "tag":"div",
                                                "ATTRIBUTES":{
                                                   "class":"iter-tabview-content iter-widget-bd",
                                                   "id":"_rankingviewerportlet_WAR_trackingportlet_INSTANCE_359b55738854406c9333d33a7de77949_tabsContent"
                                                },
                                                "children":[
                                                   {
                                                      "tag":"div",
                                                      "ATTRIBUTES":{
                                                         "class":"iter-tabview-content-item iter-tabview-content iter-widget-bd"
                                                      },
                                                      "children":[
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n1 odd first full-access iter-rankingtab-mostrecent-bd",
                                                               "iteridart":"MD4476907"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"1"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Desporto "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/desporto/arsenal-quebra-ciclo-de-13-jogos-sem-perder-do-manchester-united-MD4476907"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2082293;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Arsenal quebra ciclo de 13 jogos sem perder do Manchester United"
                                                                                 }
                                                                              ],
                                                                              "data":" "
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n2 even full-access iter-rankingtab-mostrecent-bd",
                                                               "iteridart":"KD4476590"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"2"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Desporto "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/desporto/dupla-de-arbitros-madeirenses-dirigiu-final-de-europeu-de-tenis-de-mesa-KD4476590"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2082248;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Dupla de \u00e1rbitros madeirenses dirigiu final de Europeu de t\u00e9nis de mesa"
                                                                                 }
                                                                              ],
                                                                              "data":" "
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n3 odd full-access iter-rankingtab-mostrecent-bd",
                                                               "iteridart":"CD4476532"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"3"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Madeira "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/madeira/joao-pedro-vieira-jose-quando-tiveres-candidata-e-lugar-entra-no-debate-sobre-as-eleicoes-europeias-ate-la-trabalha-CD4476532"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2082226;order=2.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Jo\u00e3o Pedro Vieira: \u201cJos\u00e9, quando tiveres candidata e lugar, entra no debate sobre as Elei\u00e7\u00f5es Europeias. At\u00e9 l\u00e1, trabalha...\u201d"
                                                                                 }
                                                                              ],
                                                                              "data":" "
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n4 even full-access iter-rankingtab-mostrecent-bd",
                                                               "iteridart":"DD4476489"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"4"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Desporto "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/desporto/sebastien-ogier-vence-rali-do-mexico-e-aproxima-se-da-lideranca-do-mundial-DD4476489"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2082216;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"S\u00e9bastien Ogier vence Rali do M\u00e9xico e aproxima-se da lideran\u00e7a do Mundial"
                                                                                 }
                                                                              ],
                                                                              "data":" "
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n5 odd full-access iter-rankingtab-mostrecent-bd",
                                                               "iteridart":"XD4476437"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"5"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Mundo "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/mundo/trump-quer-canalizar-8-6-mil-milhoes-de-dolares-para-o-muro-no-proximo-orcamento-XD4476437"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2082208;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Trump quer canalizar 8,6 mil milh\u00f5es de d\u00f3lares para o muro no pr\u00f3ximo or\u00e7amento"
                                                                                 }
                                                                              ],
                                                                              "data":" "
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n6 even last full-access iter-rankingtab-mostrecent-bd",
                                                               "iteridart":"HD4476393"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"6"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Madeira "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/madeira/antonio-costa-destaca-posicoes-ultraelegiveis-dos-candidatos-da-madeira-e-acores-HD4476393"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2082170;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Ant\u00f3nio Costa destaca posi\u00e7\u00f5es \u201cultraeleg\u00edveis\u201d dos candidatos da Madeira e A\u00e7ores"
                                                                                 }
                                                                              ],
                                                                              "data":" "
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         }
                                                      ],
                                                      "data":" "
                                                   },
                                                   {
                                                      "tag":"div",
                                                      "ATTRIBUTES":{
                                                         "class":"iter-tabview-content-item iter-helper-hidden iter-tabview-content iter-widget-bd"
                                                      },
                                                      "children":[
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n1 odd first full-access iter-rankingtab-mostviewed-bd",
                                                               "iteridart":"NX4473197"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"1"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Casos do Dia "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/casos-do-dia/homem-vitima-de-paragem-no-funchal-acabou-por-morrer-NX4473197"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2080914;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Homem v\u00edtima de \u2018paragem\u2019 no Funchal acabou por morrer"
                                                                                 }
                                                                              ],
                                                                              "data":""
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n2 even full-access iter-rankingtab-mostviewed-bd",
                                                               "iteridart":"CD4476307"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"2"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Casos do Dia "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/casos-do-dia/homem-vitima-de-overdose-no-bairro-de-santo-amaro-CD4476307"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2082162;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Homem v\u00edtima de overdose no Bairro de Santo Amaro"
                                                                                 }
                                                                              ],
                                                                              "data":""
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n3 odd full-access iter-rankingtab-mostviewed-bd",
                                                               "iteridart":"YF4474643"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"3"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Casos do Dia "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/casos-do-dia/caes-recem-nascidos-atirados-para-uma-fazenda-em-camara-de-lobos-YF4474643"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2081644;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"C\u00e3es rec\u00e9m-nascidos atirados para uma fazenda em C\u00e2mara de Lobos"
                                                                                 }
                                                                              ],
                                                                              "data":""
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n4 even full-access iter-rankingtab-mostviewed-bd",
                                                               "iteridart":"HX4473238"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"4"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Desporto "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/desporto/guarda-redes-do-moreirense-partiu-o-braco-esquerdo-HX4473238"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2080925;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Guarda-redes do Moreirense partiu o bra\u00e7o esquerdo"
                                                                                 }
                                                                              ],
                                                                              "data":""
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n5 odd full-access iter-rankingtab-mostviewed-bd",
                                                               "iteridart":"CF4474545"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"5"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Casos do Dia "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/casos-do-dia/homem-encontrado-morto-na-calheta-CF4474545"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2081620;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Homem encontrado morto na Calheta"
                                                                                 }
                                                                              ],
                                                                              "data":""
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n6 even last full-access iter-rankingtab-mostviewed-bd",
                                                               "iteridart":"MY4472349"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"6"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Casos do Dia "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/casos-do-dia/bombeiros-e-emir-tentam-salvar-homem-no-funchal-MY4472349"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2080760;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Bombeiros e EMIR tentam salvar homem no Funchal"
                                                                                 }
                                                                              ],
                                                                              "data":""
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         }
                                                      ],
                                                      "data":" "
                                                   },
                                                   {
                                                      "tag":"div",
                                                      "ATTRIBUTES":{
                                                         "class":"iter-tabview-content-item iter-helper-hidden iter-tabview-content iter-widget-bd"
                                                      },
                                                      "children":[
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n1 odd first full-access iter-rankingtab-mostcommented-bd",
                                                               "iteridart":"XA4471909"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"1"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Madeira "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/madeira/cdu-alerta-para-as-irregularidades-do-novo-hospital-privado-XA4471909"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2080378;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"CDU alerta para as irregularidades do novo hospital privado"
                                                                                 }
                                                                              ],
                                                                              "data":""
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n2 even full-access iter-rankingtab-mostcommented-bd",
                                                               "iteridart":"DA4471162"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"2"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Pa\u00eds "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/pais/neto-de-moura-insiste-que-casos-de-violencia-domestica-nao-eram-particularmente-graves-DA4471162"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2080237;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Neto de Moura insiste que casos de viol\u00eancia dom\u00e9stica n\u00e3o eram \u201cparticularmente graves\u201d"
                                                                                 }
                                                                              ],
                                                                              "data":""
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n3 odd full-access iter-rankingtab-mostcommented-bd",
                                                               "iteridart":"CF4474015"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"3"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Mundo "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/mundo/maduro-diz-que-novo-ataque-cibernetico-impediu-retorno-da-energia-CF4474015"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2081123;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Maduro diz que novo ataque \u201ccibern\u00e9tico\u201d impediu retorno da energia"
                                                                                 }
                                                                              ],
                                                                              "data":""
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n4 even full-access iter-rankingtab-mostcommented-bd",
                                                               "iteridart":"DA4471764"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"4"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Madeira "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/madeira/assuncao-cristas-diz-que-a-sondagem-da-rua-esta-muito-animadora-para-o-cds-pp-DA4471764"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2080354;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Assun\u00e7\u00e3o Cristas diz que a \u201csondagem da rua\u201d est\u00e1 \u201cmuito animadora\u201d para o CDS-PP"
                                                                                 }
                                                                              ],
                                                                              "data":""
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n5 odd full-access iter-rankingtab-mostcommented-bd",
                                                               "iteridart":"DB4470371"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"5"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Madeira "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/madeira/tragedia-do-monte-ensombra-eleicoes-DB4470371"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2079710;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"Trag\u00e9dia do Monte ensombra elei\u00e7\u00f5es"
                                                                                 }
                                                                              ],
                                                                              "data":""
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         },
                                                         {
                                                            "tag":"div",
                                                            "ATTRIBUTES":{
                                                               "class":"element n6 even last full-access iter-rankingtab-mostcommented-bd",
                                                               "iteridart":"FX4473362"
                                                            },
                                                            "children":[
                                                               {
                                                                  "tag":"span",
                                                                  "ATTRIBUTES":{
                                                                     "class":"teaserItemPosition"
                                                                  },
                                                                  "children":[

                                                                  ],
                                                                  "data":"6"
                                                               },
                                                               {
                                                                  "tag":"h3",
                                                                  "ATTRIBUTES":{
                                                                     "class":"template-19"
                                                                  },
                                                                  "children":[
                                                                     {
                                                                        "tag":"div",
                                                                        "ATTRIBUTES":{
                                                                           "class":"section small"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"span",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"assigned-section"
                                                                              },
                                                                              "children":[

                                                                              ],
                                                                              "data":"Madeira "
                                                                           }
                                                                        ],
                                                                        "data":""
                                                                     },
                                                                     {
                                                                        "tag":"a",
                                                                        "ATTRIBUTES":{
                                                                           "href":"/madeira/jsd-quer-maior-proximidade-popular-e-aposta-na-vitoria-do-psd-nas-eleicoes-deste-ano-FX4473362"
                                                                        },
                                                                        "children":[
                                                                           {
                                                                              "tag":"h3",
                                                                              "ATTRIBUTES":{
                                                                                 "class":"headline font-1 extra-small bold"
                                                                              },
                                                                              "children":[
                                                                                 {
                                                                                    "tag":"span",
                                                                                    "ATTRIBUTES":{
                                                                                       "class":"priority-content",
                                                                                       "mlnid":"idcon=2080958;order=1.0"
                                                                                    },
                                                                                    "children":[

                                                                                    ],
                                                                                    "data":"JSD quer maior proximidade popular e aposta na vit\u00f3ria do PSD nas elei\u00e7\u00f5es deste ano"
                                                                                 }
                                                                              ],
                                                                              "data":""
                                                                           }
                                                                        ],
                                                                        "data":" "
                                                                     }
                                                                  ],
                                                                  "data":" "
                                                               }
                                                            ],
                                                            "data":" "
                                                         }
                                                      ],
                                                      "data":" "
                                                   }
                                                ],
                                                "data":" "
                                             }
                                          ],
                                          "data":" "
                                       }
                                    ],
                                    "data":" "
                                 }
                              ],
                              "data":" "
                           }
                        ],
                        "data":" "
                     }
                  ],
                  "data":" "
               }
            ],
            "data":" "
         }
      ],
      "data":" "
   }
]
        parser = JsonHtmlParser()
        parser.feed(content)
        print(parser.get_content())
        self.assertEqual(parser.get_content(), json.dumps(result))

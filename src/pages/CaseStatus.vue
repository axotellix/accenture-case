
<!-- [ TEMPLATE ] -->
<template>

    <!-- [ page: case status ] -->
    <main>
        <article>
            <!-- heading -->
            <h2 class = 'heading mt-50'>Статус портфеля</h2>

            <!-- problem stated -->
            <section>
                <h6 class = 'caption'>Проблема</h6>
                <p v-if="this.case_status==0"  class = 'mark text-red'>Портфель не сбалансирован</p>
                <p v-if="this.case_status==1" class = 'mark text-green'>Портфель сбалансирован</p>
            </section>

            <!-- infographics -->
            <section class = 'col-2'>
                <!-- infographics: your case -->
                <div class="group">
                    <h6 class = 'caption mb-20'>Ваш портфель:</h6>
                    <div class = 'infographics-container'>
                        <Infographics
                            colour="red"
                            subject="Акции"
                            :estimation="this.assets_count.bonds_total"
                            :total="this.assets_count.total"
                            measurement_sign="%"
                        />
                        <Infographics
                            colour="purple"
                            subject="Облигации"
                            :estimation="this.assets_count.stocks_total"
                            :total="this.assets_count.total"
                            measurement_sign="%"
                        />
                    </div>
                </div>
                <!-- infographics: goal case -->
                <div class="group">
                    <h6 class = 'caption mb-20'>Целевой портфель:</h6>
                    <div class = 'infographics-container'>
                        <Infographics
                            colour="red"
                            subject="Акции"
                            :estimation="this.case_reference.bonds"
                            measurement_sign="%"
                        />
                        <Infographics
                            colour="purple"
                            subject="Облигации"
                            :estimation="this.case_reference.stocks"
                            measurement_sign="%"
                        />
                    </div>
                </div>
            </section>

            <!-- problem solution -->
            <section>
                <h6 class = 'caption'>Решение</h6>
                <p class = 'mark text-green'>Докупить облигаций</p>

                <p class = 'description'>
                    {{  this.message }}
                </p>
            </section>
        </article>

        <article>
            <!-- heading -->
            <h2 class = 'heading'>Подходит для Вашей цели</h2>

            <div class="group flex flex-row gap-small">
                <Card 
                    :key="asset_type"
                    v-for="asset_type in this.assets_to_buy"
                    :title="this.assets_types[asset_type]" :colour="this.assets_colours[asset_type]"
                >
                    <template v-slot:note>
                        Необходимо: <span>&#8381; 247 000</span>
                    </template>
                    <template v-slot:content>
                        <Asset 
                            :key="company" 
                            :company="company"
                            v-for="company in this.assets[asset_type]"
                            status = 'up' 
                        />
                    </template>
                </Card>
            </div>
        </article>
    </main>

</template>


<!-- [ SCRIPTS ] -->
<script>
import Infographics from './../components/Infographics'
import Card from './../components/Card'
import Asset from './../components/Asset'

export default {
    // [ Component name ]
    name: 'CaseStatus',

    // [ Child components ]
    components: {
        Infographics,
        Card,
        Asset,
    },

    // [ Properties ]
    props: {
        active_user: String
    },

    // [ data ]
    data() {
        return {
            case_status: 0,
            message: '',
            to_buy: {},
            assets_to_buy: [],
            assets_types: {
                "bonds": "Акции",
                "stocks": "Облигации",
            },
            assets_colours: {
                "bonds": "red",
                "stocks": "purple",
            },
            assets: {
                bonds: [],
                stocks: [],
            },
            assets_count: {
                total: 0,
                bonds_total: 0, 
                stocks_total: 0, 
            },
            case_reference: {
                bonds: 0, 
                stocks: 0, 
            }
        }
    },

    // [ on: create ]
    async created() {
        // get > person data
        let req  = await fetch('https://axotellix.pythonanywhere.com/api/rebalance/' + this.active_user);
        let case_summary = await req.json();

        console.log(case_summary);

        // get > case summary
        let status  = case_summary.status;
        let message = case_summary.description;
        let to_buy  = case_summary.to_buy; 

        this.case_status = status;
        this.message     = message;
        this.to_buy      = to_buy;

        Object.keys(to_buy).forEach(asset => {
            if( to_buy[asset] ) {
                this.assets_to_buy.push(asset);
            }
        });

        // get > bonds & stocks
        let bonds  = case_summary.bonds;
        let stocks = case_summary.stocks;

        this.assets.bonds  = bonds;
        this.assets.stocks = stocks;

        // count > assets
        req        = await fetch('https://axotellix.pythonanywhere.com/api/userinfo/' + this.active_user);
        let person = await req.json();

        let assets_total = person.assets_total;
        let bonds_total  = person.bonds_total;
        let stocks_total = person.stocks_total;
        
        let risk_profile = person.type;
        let bonds_ref  = 50;
        let stocks_ref = 50;

        switch( risk_profile ) {
            case 1:
                bonds_ref  = 0;
                stocks_ref = 100;
                break;
            case 2:
                bonds_ref  = 20;
                stocks_ref = 80;
                break;
            case 3:
                bonds_ref  = 50;
                stocks_ref = 50;
                break;
            case 4:
                bonds_ref  = 30;
                stocks_ref = 70;
                break;
            case 5:
                bonds_ref  = 0;
                stocks_ref = 100;
                break;
        }

        this.assets_count.total        = assets_total;
        this.assets_count.bonds_total  = bonds_total;
        this.assets_count.stocks_total = stocks_total;

        this.case_reference.bonds  = bonds_ref;
        this.case_reference.stocks = stocks_ref;
    }
}
</script>


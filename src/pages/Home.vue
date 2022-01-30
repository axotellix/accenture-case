
<!-- [ TEMPLATE ] -->
<template>

    <!-- [ page: home ] -->
    <main>
        <article>
            <!-- heading -->
            <h2 class = 'heading'>Мой портфель</h2>

            <div class="group flex flex-row gap-small">
                <!-- bonds -->
                <Card title = 'Акции' colour = 'red'>
                    <template v-slot:content>
                        <Asset 
                            :key="company" 
                            :company="company"
                            v-for="company in this.assets.bonds_companies" 
                            status = 'up' 
                        />
                    </template>
                </Card>
                <!-- stocks -->
                <Card title = 'Облигации' colour = 'purple'>
                    <template v-slot:content>
                        <Asset 
                            :key="company" 
                            :company="company"
                            v-for="company in this.assets.stocks_companies" 
                            status = 'up' 
                        />
                    </template>
                </Card>
            </div>
        </article>

        <article>
            <!-- heading -->
            <h2 class = 'heading mt-50'>Мой портфель. Состав</h2>

            <ul class="tabs">
                <li class = 'tab-item active'>Активы</li>
                <li class = 'tab-item'>Компании</li>
                <li class = 'tab-item'>Отрасли</li>
                <li class = 'tab-item'>Облигации</li>
            </ul>
            <!-- case: my assets -->
            <MyAssets />
        </article>
    </main>

</template>


<!-- [ SCRIPTS ] -->
<script>
import Card from './../components/Card'
import Asset from './../components/Asset'
import MyAssets from './../components/mycase/MyAssets'

export default {
    // [ Component name ]
    name: 'Home',

    // [ Child components ]
    components: {
        Card,
        Asset,
        MyAssets,
    },

    props: {
        active_user: String,
    },

    // [ data ]
    data() {
        return {
            assets: {
                bonds: {},
                stocks: {},
                bonds_companies: [],
                stocks_companies: [],
            }
        }
    },

    // [ on: create ]
    async created() {
        // get > person data
        let req = await fetch('https://axotellix.pythonanywhere.com/api/userinfo/' + this.active_user);
        let person = await req.json();

        // get > bonds & stocks
        let bonds  = person?.bonds || {};
        let stocks = person?.stocks || {};

        this.assets.bonds  = bonds;
        this.assets.stocks = stocks;

        this.assets.bonds_companies  = Object.keys(bonds) ?? [];
        this.assets.stocks_companies = Object.keys(stocks) ?? [];
    }
}
</script>

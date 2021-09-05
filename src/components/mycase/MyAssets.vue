
<!-- [ TEMPLATE ] -->
<template>

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

</template>


<!-- [ SCRIPTS ] -->
<script>
import Infographics from './../Infographics'

export default {
    // [ Component name ]
    name: 'MyAssets',

    // [ Child components ]
    components: {
        Infographics,
    },

    // [ data ]
    data() {
        return {
            assets_types: {
                "bonds": "Акции",
                "stocks": "Облигации",
            },
            assets_colours: {
                "bonds": "red",
                "stocks": "purple",
            },
            assets_count: {
                total: 0,
                bonds_total: 0, 
                stocks_total: 0, 
            }
        }
    },

    // [ on: create ]
    async created() {
        // get > person data
        let req    = await fetch('https://reworr.pythonanywhere.com/api/userinfo/user1');
        let person = await req.json();

        // get > case summary

        // get > bonds & stocks
        let assets_total = person.assets;
        let bonds_total  = person.bonds_count;
        let stocks_total = person.stocks_count;

        this.assets_count.total        = assets_total;
        this.assets_count.bonds_total  = bonds_total;
        this.assets_count.stocks_total = stocks_total;

    }
}
</script>


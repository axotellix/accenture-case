
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
                            estimation=70
                            measurement_sign="%"
                        />
                        <Infographics
                            colour="purple"
                            subject="Облигации"
                            estimation=30
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
                            estimation=60
                            measurement_sign="%"
                        />
                        <Infographics
                            colour="purple"
                            subject="Облигации"
                            estimation=40
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

            <Card title = 'Облигации' colour = 'purple'>
                <template v-slot:note>
                    Необходимо: <span>&#8381; 247 000</span>
                </template>
                <template v-slot:content>
                    <Asset status = 'up' />
                    <Asset status = 'down' />
                </template>
            </Card>
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

    // [ data ]
    data() {
        return {
            case_status: 0,
            message: '',
        }
    },

    // [ on: create ]
    async created() {
        // get > person data
        let req  = await fetch('https://reworr.pythonanywhere.com/api/rebalance/user1');
        let case_summary = await req.json();

        // get > case summary
        let status  = case_summary.status;
        let message = case_summary.description;

        this.case_status = status;
        this.message     = message;

        console.log(status);
    }
}
</script>


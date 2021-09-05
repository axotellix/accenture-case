
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
                <p v-if="true"  class = 'mark text-red'>Портфель не сбалансирован</p>
                <p v-if="false" class = 'mark text-green'>Портфель сбалансирован</p>
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
                    Портфель состоит на 70% из акций и на 30% из облигаций. <br><br>
                    Закупка 76 облигаций ОФЗ сделает ваш портфель более сбалансированным и снизит риски, что соответствует Вашей цели.
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
    }
}
</script>


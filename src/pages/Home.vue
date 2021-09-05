
<!-- [ TEMPLATE ] -->
<template>

    <!-- [ page: home ] -->
    <main>
        <article>
            <!-- heading -->
            <h2 class = 'heading mt-50'>Мой портфель</h2>

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
        </article>

        <article>
            <!-- heading -->
            <h2 class = 'heading'>Мой портфель</h2>

            <div class="group flex flex-row gap-small">
                <!-- bonds -->
                <Card title = 'Акции' colour = 'red'>
                    <template v-slot:content>
                        <Asset status = 'up' />
                        <Asset status = 'down' />
                    </template>
                </Card>
                <!-- shares -->
                <Card title = 'Фонды' colour = 'orange'>
                    <template v-slot:content>
                        <Asset status = 'up' />
                        <Asset status = 'down' />
                    </template>
                </Card>
                <!-- stocks -->
                <Card title = 'Облигации' colour = 'purple'>
                    <template v-slot:content>
                        <Asset status = 'up' />
                        <Asset status = 'down' />
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
import Infographics from './../components/Infographics'
import Card from './../components/Card'
import Asset from './../components/Asset'
import MyAssets from './../components/mycase/MyAssets'

export default {
    // [ Component name ]
    name: 'Home',

    // [ Child components ]
    components: {
        Infographics,
        Card,
        Asset,
        MyAssets,
    }
}
</script>



<!-- [ TEMPLATE ] -->
<template>

    <!-- [ page: case status ] -->
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

            <Card title = 'Облигации' colour = 'purple'>
                <Asset status = 'up' />
                <Asset status = 'down' />
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
    name: 'Home',

    // [ Child components ]
    components: {
        Infographics,
        Card,
        Asset,
    }
}
</script>


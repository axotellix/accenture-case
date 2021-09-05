
<!-- [ TEMPLATE ] -->
<template>

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
    }
}
</script>




<!-- [ TEMPLATE ] -->
<template>

    <!-- [ card ] -->
    <div class="asset">
        <div class="company-info">
            <div class="company-logo"></div>
            <div class="company-name">Company Name</div>
        </div>
        <div :class="'quotes ' + this.status">
            <Ico type="arrow-right" /> 0.25$ / 0.20%
        </div>
    </div>

</template>


<!-- [ SCRIPTS ] -->
<script>
import Ico from './Ico'

export default {
    // [ Component name ]
    name: 'Asset',

    // [ Child components ]
    components: {
        Ico,
    },

    // [ Properties ]
    props: {
        status: {
            type: String,
            default: 'up'
        },
    }
}
</script>


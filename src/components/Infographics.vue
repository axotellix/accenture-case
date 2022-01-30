
<!-- [ TEMPLATE ] -->
<template>

    <!-- [ page: case status ] -->
    <div class="infographics" :colour="this.colour">
        <!-- estimation -->
        <div class="estimation">
            {{ Math.round((this.estimation || 0) / (this.total || 100) * 100) + (this.measurement_sign || '%') }}
        </div>

        <!-- progress bar -->
        <div class="progressbar" :data-caption="this.subject">
            <div class = 'activebar' :style="'width:' + (this.estimation || 0) / (this.total || 100) * 100 + '%'"></div>
        </div>
    </div>

</template>


<!-- [ SCRIPTS ] -->
<script>
export default {
    // [ Component name ]
    name: 'Infographics',

    // [ Properties ]
    props: {
        colour: {
            type: String,
            default: 'purple'
        },
        subject: {
            type: String,
            default: 'Актив'
        },
        total: {
            type: Number,
            default: 100
        },
        estimation: {
            type: Number,
            default: 0
        },
        measurement_sign: {
            type: String,
            default: '%'
        },
        
    },
}
</script>


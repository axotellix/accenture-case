
<!-- [ TEMPLATE ] -->
<template>


    <!-- ico: arrow (right) -->
    <svg v-if="this.type == 'arrow-right'" class="ico">
        <use xlink:href="/img/sprites.svg#ico-arrow"></use>
    </svg>

    <!-- ico: plus -->
    <svg v-if="this.type == 'plus'" class="ico">
        <use xlink:href="/img/sprites.svg#ico-plus"></use>
    </svg>


</template>


<!-- [ SCRIPTS ] -->
<script>
export default {
    name: 'App',
    
    // [ Properties ]
    props: ['type'],

}
</script>


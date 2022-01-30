
<!-- [ TEMPLATE ] -->
<template>
    <div class = 'header-card'>

        <!-- card caption -->
        <h6 class="caption">{{ title }}</h6>

        <!-- card content -->
        <div class="card-content">
            <slot></slot>
        </div>

    </div>
</template>


<!-- [ SCRIPTS ] -->
<script>
export default {
    // [ Component name ]
    name: 'HeaderCard',

    // [ Properties ]
    props: {
        title: {
            type: String,
            default: 'Показатель'
        }
    }
}
</script>
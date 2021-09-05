
<!-- [ TEMPLATE ] -->
<template>
    <div class='avatar'>

        <!-- img: person avatar -->
        <div class='ava-img'></div>

        <!-- caption: person name -->
        <p class='caption'>{{ this.name }}</p>

    </div>
</template>


<!-- [ SCRIPTS ] -->
<script>

export default {
    // [ Component name ]
    name: 'Avatar',

    // [ Properties ]
    props: {
        name: String,
        ava: String,
    }
}
</script>


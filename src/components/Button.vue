
<!-- [ TEMPLATE ] -->
<template>
    <div class = 'button'>

        <slot></slot>

    </div>
</template>


<!-- [ SCRIPTS ] -->
<script>
export default {
    // [ Component name ]
    name: 'Button',

    // [ Properties ]
    props: {
        msg: String
    }
}
</script>
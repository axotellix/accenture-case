

<!-- [ TEMPLATE ] -->
<template>

    <!-- [ card ] -->
    <div class="card-big" :colour="this.colour">
        <!-- card decor -->
        <div class="blur-circle circle-top"></div>

        <!-- card header -->
        <div class="card-header">
            <h3 class="card-title">{{ title }}</h3>
            <p class="card-note">
                <slot name = 'note'></slot>
            </p>
        </div>

        <!-- card wrapper -->
        <div class="card-wrapper">
            <!-- card decor -->
            <div class="blur-circle circle-bottom"></div>

            <div class="card-content">
                <slot name = 'content'></slot>
            </div>
            <div class="card-footer">
                <a href="" class="cta">
                    <span>смотреть все</span>
                    <Button :class="this.colour">
                        <Ico type="arrow-right" />
                    </Button>
                </a>
            </div>
        </div>
    </div>

</template>


<!-- [ SCRIPTS ] -->
<script>
import Button from './Button'
import Ico from './Ico'

export default {
    // [ Component name ]
    name: 'Card',

    // [ Child components ]
    components: {
        Button,
        Ico,
    },

    // [ Properties ]
    props: {
        colour: {
            type: String,
            default: 'purple'
        },
        title: {
            type: String,
            default: 'Актив'
        },
    }
}
</script>


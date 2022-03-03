const styles = theme => ({
    notificationStyle: {
        display: 'flex',
        borderRadius: '5px',
        width: '500px',
        height:'80px',
        cursor: 'pointer',
        flexDirection: 'row',
        alignItems: 'center',
        backgroundColor: '#FFFFFF',
        paddingTop: '0px',
        paddingBottom: '0px',
        justifyContent: 'space-evenly',
        '&:hover': {
            '& $viewDot': {
                backgroundColor: '#F9D967',
            },
            '& $message': {
                color: '#FFFFFF',
            },
            '& $time': {
                color: '#FFFFFF',
            },
            '& $image': {
                backgroundColor: 'white',

            },
            backgroundColor: '#52B5C2',
            fontColor: '#FFFFFF',
        },
    },
    image: {
        width: '56px !important',
        height: '56px !important',
        borderRadius: '50%',
        backgroundColor: '#00B8C4',
        margin: '0px',
        border: '0px',
        padding: '0px',
    },
    message: {
        fontSize: '16px',
        font: 'Raleway',
        color: '#000000',
        marginBottom: '0px',
        '&:hover': {
            color: '#FFFFFF',
        },
    },
    time: {
        marginTop: '0px',
        fontSize: '14px',
        color: '#00B8C4',
        '&:hover': {
            color: '#FFFFFF',
        },
    },
    viewDot: {
        backgroundColor: '#00B8C4',
        borderRadius: '50%',
        width: '14px',
        height: '14px',
        '&:hover': {
            backgroundColor: '#F9D967',
        },
    },
});

export default styles;

window.Parsley.addValidator('cve', {
    validateString: function(value) {
        let match = value.match(/CVE-\d{4}-\d{4,7}/i) || false;
        return match;
    },
    messages: {
        en: 'cve is not valid'
    }
});
window.Parsley.addValidator('ip', {
    validateString: function(value) {
        let match = value.match(/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/g) || false;
        return match;
    },
    messages: {
        en: 'cve is not valid'
    }
});
window.Parsley.addValidator('port', {
    validateString: function(value) {
        let match = value.match(/^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$/g) || false;
        return match;
    },
    messages: {
        en: 'cve is not valid'
    }
});
window.Parsley.addValidator('uppercase', {
    validateString: function(value, requirement) {
        var uppercase = value.match(/[A-Z]/g) || [];
        return uppercase.length >= requirement;
    },
    messages: {
        en: 'Your password must contain at least (%s) uppercase letter.'
    }
});
//has lowercase
window.Parsley.addValidator('lowercase', {
    validateString: function(value, requirement) {
        var lowecases = value.match(/[a-z]/g) || [];
        return lowecases.length >= requirement;
    },
    messages: {
        en: 'Your password must contain at least (%s) lowercase letter.'
    }
});

//has number
window.Parsley.addValidator('number', {
    validateString: function(value, requirement) {
        var numbers = value.match(/[0-9]/g) || [];
        return numbers.length >= requirement;
    },
    messages: {
        en: 'Your password must contain at least (%s) number.'
    }
});

//has special char
window.Parsley.addValidator('special', {
    validateString: function(value, requirement) {
        var specials = value.match(/[^a-zA-Z0-9]/g) || [];
        return specials.length >= requirement;
    },
    messages: {
        en: 'Your password must contain at least (%s) special characters.'
    }
});

//has special char
window.Parsley.addValidator('nationalnumber', {
    validateString: function(value) {
        value = value.replace(/-/g, "");
        if (!/^\d{10}$/.test(value)
            || value=='0000000000'
            || value=='1111111111'
            || value=='2222222222'
            || value=='3333333333'
            || value=='4444444444'
            || value=='5555555555'
            || value=='6666666666'
            || value=='7777777777'
            || value=='8888888888'
            || value=='9999999999')
                return false;
            var check = parseInt(value[9]);
            var sum = 0;
            var i;
            for (i = 0; i < 9; ++i) {
                sum += parseInt(value[i]) * (10 - i);
            }
            sum %= 11;
            return (sum < 2 && check == sum) || (sum >= 2 && check + sum == 11);
    },
    messages: {
        fa: 'شماره ملی وارد شده صحیح نیست'
    }
});